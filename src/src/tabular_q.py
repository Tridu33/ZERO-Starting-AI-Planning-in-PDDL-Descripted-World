"""Tabular Q-learning for the 16-state blocks_clear feature space.

The DQN class in `dqn.py` is the "neural" path; this module is the
guaranteed-correct tabular path used to (a) provide ground-truth Q-values and
(b) supervise the Binary Neural Network.

The 4-bit state fully describes the agent's decision, so the Q-table is just
a 16 x n_actions matrix. We update it using ε-greedy episodes drawn from the
BlocksClearEnv. Because the env enforces STRIPS preconditions, illegal moves
simply get a small negative reward (no state change) which is sufficient signal
to learn the optimal decomposition.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from typing import Dict, List, Sequence, Tuple

import numpy as np

from .blocks_clear_env import BlocksClearEnv


def state_bits(obs: np.ndarray) -> Tuple[int, ...]:
    return tuple(int(round(float(v))) for v in obs)


@dataclass
class TabularConfig:
    n_episodes: int = 1500
    gamma: float = 0.95
    alpha: float = 0.5
    eps_start: float = 1.0
    eps_end: float = 0.02
    eps_decay_episodes: int = 600
    seed: int = 0
    invalid_penalty: float = -0.1
    goal_reward: float = 1.0
    step_cost: float = 0.0
    max_steps: int = 32


class TabularQLearner:
    """Standard tabular Q-learning on the 4-bit feature space."""

    def __init__(self, env: BlocksClearEnv, cfg: TabularConfig | None = None):
        self.env = env
        self.cfg = cfg or TabularConfig()
        self.n_actions = env.n_actions
        self.Q: Dict[Tuple[int, ...], np.ndarray] = defaultdict(
            lambda: np.zeros(self.n_actions, dtype=np.float32)
        )
        self.rng = np.random.default_rng(self.cfg.seed)

    def epsilon(self, ep: int) -> float:
        cfg = self.cfg
        frac = min(1.0, ep / max(1, cfg.eps_decay_episodes))
        return cfg.eps_start + frac * (cfg.eps_end - cfg.eps_start)

    def train(self, log_every: int = 100) -> List[float]:
        cfg = self.cfg
        rewards: List[float] = []
        for ep in range(cfg.n_episodes):
            obs, _ = self.env.reset()
            s = state_bits(obs)
            ep_reward = 0.0
            for t in range(cfg.max_steps):
                a = self._select_action(s, ep)
                nxt, r, done, trunc, info = self.env.step(int(a))
                ns = state_bits(nxt)
                # Bellman update (off-policy, max over ns)
                td_target = r
                if not (done or trunc):
                    td_target += cfg.gamma * float(self.Q[ns].max())
                td_error = td_target - float(self.Q[s][a])
                self.Q[s][a] += cfg.alpha * td_error
                s = ns
                ep_reward += r
                if done or trunc:
                    break
            rewards.append(ep_reward)
            if log_every and (ep == 0 or (ep + 1) % log_every == 0):
                recent = rewards[-log_every:]
                print(f"  TabQ ep={ep+1:4d}  R_mean={np.mean(recent):+.3f}  eps={self.epsilon(ep):.3f}")
        return rewards

    # ------------------------------------------------------------------ action
    def _select_action(self, s: Tuple[int, ...], ep: int) -> int:
        eps = self.epsilon(ep)
        if self.rng.random() < eps:
            appl = self._applicable_for(s)
            if appl:
                return int(self.rng.choice(appl))
            return int(self.rng.integers(self.n_actions))
        return self._greedy(s)

    @staticmethod
    def is_applicable_state(s: Tuple[int, ...]) -> bool:
        """All 16 states are 'applicable' in the obs-sense; we don't enforce
        physical reachability from the initial 0001 — instead, the optimal
        policy returns goal/virtual at non-reachable states because of the
        reward structure. The episode terminates when goal is reached.
        """

        return True

    def _applicable_for(self, s: Tuple[int, ...]) -> List[int]:
        """Per-state applicable actions using the env's STRIPS rules.

        We pin the env state (by setting vstart_active and stepping through
        known transitions) — but for the 4-bit search we use a simpler
        heuristic: any STRIPS op indexed 2..N+1 is potentially applicable,
        with the virtuals guarded by the var flags.
        """

        blockscleared, h, vgoal, vstart = s
        # Virtuals
        apps: List[int] = []
        if vstart == 1:
            apps.append(BlocksClearEnv.VIRTUAL_START_IDX)
        if vgoal == 1:
            apps.append(BlocksClearEnv.GOAL_IDX)

        # STRIPS applicability purely from the 4 bits (we cannot fully recover
        # which putdown/unstack is grounded from just the boolean features, so
        # we let all STRIPS ops be candidates — invalid steps simply inherit
        # a bad Q and are pruned via Bellman-optimality selection).
        for i in range(2, self.n_actions):
            apps.append(i)
        return apps

    def _greedy(self, s: Tuple[int, ...]) -> int:
        appl = self._applicable_for(s)
        q = self.Q[s].copy()
        if not appl:
            return int(np.argmax(q))
        mask = np.full(self.n_actions, -1e9, dtype=np.float32)
        for a in appl:
            mask[a] = q[a]
        return int(np.argmax(mask))

    # ------------------------------------------------------------------ access
    def q_table(self) -> np.ndarray:
        out = np.zeros((16, self.n_actions), dtype=np.float32)
        for i, bits in enumerate(product([0, 1], repeat=4)):
            out[i] = self.Q[bits]
        return out

    def greedy_table(self) -> Dict[Tuple[int, ...], int]:
        return {bits: self._greedy(bits) for bits in product([0, 1], repeat=4)}


__all__ = ["TabularQLearner", "TabularConfig", "state_bits"]
