"""DQN agent for the 4-feature Blocks_clear domain.

由于状态空间极小 (4 维布尔 → 16 个 state), 一个 **tabular** DQN 完全够用;
但我们仍然使用一个小的 MLP (两层) 以展现"训练 Q 网络 -> 导出 Q-table"
的转换路径。Episode 累积后, 我们遍历全部 16 个布尔状态, 让 DQN 输出
Q-values 作为 final Q-table。

该 Q-table 与人类策略一致时应满足:
    Q(0,0,0,1) → vstart      idx
    Q(0,0,0,0) → unstack     idx
    Q(0,1,0,0) → putdown     idx
    Q(1,?,1,?) → goal        idx

其它 12 个状态在规划域下不可达 / dead-end, DQN 仍给出 argmax,
但 PRP 策略中 by-construction 不会进入它们 (从初态 0001 通过确定性转移)。
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# Q-Network: small MLP (4 -> 32 -> 32 -> n_actions)
# ---------------------------------------------------------------------------
class QNet(nn.Module):
    def __init__(self, in_dim: int = 4, hidden: int = 32, n_actions: int = 11):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, n_actions),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


# ---------------------------------------------------------------------------
# Hyperparameters
# ---------------------------------------------------------------------------
@dataclass
class DQNConfig:
    n_episodes: int = 600
    max_steps_per_episode: int = 32
    gamma: float = 0.95
    lr: float = 1e-3
    batch_size: int = 32
    buffer_size: int = 4096
    eps_start: float = 1.0
    eps_end: float = 0.05
    eps_decay_steps: int = 1500
    target_sync_steps: int = 100
    learning_starts: int = 200
    seed: int = 0
    hidden: int = 32


# ---------------------------------------------------------------------------
# DQN Agent
# ---------------------------------------------------------------------------
class DQNAgent:
    def __init__(
        self,
        env,
        n_actions: int,
        cfg: Optional[DQNConfig] = None,
        device: str = "cpu",
    ) -> None:
        self.env = env
        self.n_actions = n_actions
        self.cfg = cfg or DQNConfig()
        self.device = torch.device(device)

        torch.manual_seed(self.cfg.seed)
        np.random.seed(self.cfg.seed)

        self.q_net = QNet(in_dim=4, hidden=self.cfg.hidden, n_actions=n_actions).to(self.device)
        self.target_net = QNet(in_dim=4, hidden=self.cfg.hidden, n_actions=n_actions).to(self.device)
        self.target_net.load_state_dict(self.q_net.state_dict())
        for p in self.target_net.parameters():
            p.requires_grad = False

        self.optim = torch.optim.Adam(self.q_net.parameters(), lr=self.cfg.lr)

        self.buffer: deque = deque(maxlen=self.cfg.buffer_size)
        self.global_step = 0
        self.epsilon = self.cfg.eps_start

    # ------------------------------------------------------------------ act
    def _epsilon_threshold(self) -> float:
        cfg = self.cfg
        frac = min(1.0, self.global_step / max(1, cfg.eps_decay_steps))
        return cfg.eps_start + frac * (cfg.eps_end - cfg.eps_start)

    def select_action(self, obs: np.ndarray, *, deterministic: bool = False) -> int:
        self.epsilon = self._epsilon_threshold()
        if (not deterministic) and np.random.rand() < self.epsilon:
            return int(np.random.randint(self.n_actions))

        # Restrict to applicable actions to avoid invalid moves dominating replay.
        applicable = self.env.applicable_indices(include_virtual=True)
        with torch.no_grad():
            x = torch.tensor(obs, dtype=torch.float32, device=self.device).unsqueeze(0)
            q = self.q_net(x).squeeze(0).cpu().numpy()
        if applicable:
            mask = np.full(self.n_actions, -1e9, dtype=np.float32)
            mask[applicable] = q[applicable]
            return int(np.argmax(mask))
        return int(np.argmax(q))

    # ------------------------------------------------------------------ learn
    def _buffer_push(self, s, a, r, ns, done) -> None:
        self.buffer.append((s, a, r, ns, done))

    def _optimize(self) -> Optional[float]:
        if len(self.buffer) < self.cfg.learning_starts:
            return None
        cfg = self.cfg
        idxs = np.random.choice(len(self.buffer), size=cfg.batch_size, replace=False)
        s = torch.tensor(np.stack([self.buffer[i][0] for i in idxs]), dtype=torch.float32, device=self.device)
        a = torch.tensor([self.buffer[i][1] for i in idxs], dtype=torch.long, device=self.device).unsqueeze(1)
        r = torch.tensor([self.buffer[i][2] for i in idxs], dtype=torch.float32, device=self.device)
        ns = torch.tensor(np.stack([self.buffer[i][3] for i in idxs]), dtype=torch.float32, device=self.device)
        done = torch.tensor([float(self.buffer[i][4]) for i in idxs], dtype=torch.float32, device=self.device)

        with torch.no_grad():
            target_q = self.target_net(ns).max(dim=1)[0]
            target = r + cfg.gamma * target_q * (1.0 - done)

        q_pred = self.q_net(s).gather(1, a).squeeze(1)
        loss = F.smooth_l1_loss(q_pred, target)
        self.optim.zero_grad()
        loss.backward()
        self.optim.step()
        return float(loss.item())

    # ------------------------------------------------------------------ train
    def train(self, log_every: int = 50) -> List[float]:
        cfg = self.cfg
        rewards: List[float] = []
        episode_losses: List[float] = []

        for ep in range(cfg.n_episodes):
            obs, _ = self.env.reset()
            ep_reward = 0.0
            ep_loss = 0.0
            n_loss = 0
            for t in range(cfg.max_steps_per_episode):
                a = self.select_action(obs)
                nxt, r, done, trunc, info = self.env.step(a)
                self._buffer_push(obs, a, r, nxt, done or trunc)
                obs = nxt
                ep_reward += r
                self.global_step += 1

                # Sync target
                if self.global_step % cfg.target_sync_steps == 0:
                    self.target_net.load_state_dict(self.q_net.state_dict())

                loss = self._optimize()
                if loss is not None:
                    ep_loss += loss
                    n_loss += 1

                if done or trunc:
                    break
            rewards.append(ep_reward)
            episode_losses.append(ep_loss / max(1, n_loss))
            if log_every and (ep == 0 or (ep + 1) % log_every == 0):
                recent = rewards[-log_every:]
                print(
                    f"  DQN ep={ep+1:4d}  R_mean={np.mean(recent):+.3f}  "
                    f"loss={episode_losses[-1]:.4f}  eps={self.epsilon:.3f}"
                )
        return rewards

    # ------------------------------------------------------------------ eval
    @torch.no_grad()
    def q_values(self, obs: np.ndarray) -> np.ndarray:
        x = torch.tensor(obs, dtype=torch.float32, device=self.device).unsqueeze(0)
        return self.q_net(x).squeeze(0).cpu().numpy()

    def greedy_action(self, obs: np.ndarray) -> int:
        applicable = self.env.applicable_indices(include_virtual=True)
        q = self.q_values(obs)
        if applicable:
            mask = np.full(self.n_actions, -1e9, dtype=np.float32)
            mask[applicable] = q[applicable]
            return int(np.argmax(mask))
        return int(np.argmax(q))

    def greedy_action_table(self) -> Dict[Tuple[int, ...], int]:
        """Return argmax_a Q(s,a) for all 16 binary states."""

        table: Dict[Tuple[int, ...], int] = {}
        for bits in product([0, 1], repeat=4):
            obs = np.array(bits, dtype=np.float32)
            table[bits] = self.greedy_action(obs)
        return table

    def q_table(self) -> np.ndarray:
        """Return shape (16, n_actions) — full Q-table over the 16 binary states."""

        n = self.n_actions
        qtab = np.zeros((16, n), dtype=np.float32)
        for i, bits in enumerate(product([0, 1], repeat=4)):
            obs = np.array(bits, dtype=np.float32)
            qtab[i] = self.q_values(obs)
        return qtab


__all__ = ["DQNAgent", "DQNConfig", "QNet"]
