"""Brevitas Binary Neural Network for the blocks_clear policy.

Architecture
------------
- Input (4) — to be fed as 0/1 floats
- QuantLinear(4 -> 16, weight_bit_width=1)
- QuantIdentity (binary activation)
- QuantLinear(16 -> 32, weight_bit_width=1)
- QuantIdentity (binary activation)
- QuantLinear(32 -> n_actions, bias=True, weight_bit_width=1)  ← output layer

Training
--------
Two supervision signals supported:
1. Behaviour cloning on the converged Q-table: target = Q[s] (regression on Q-values).
2. Policy-only distillation: target = one-hot of argmax Q[s] (cross-entropy).

Both loss types are reduced to a single MSE / CE on the small dataset
(16 samples), which suffices because the policy is purely a function of the
4-bit state.

Equivalence check
-----------------
After training, we enumerate all 16 binary states, forward through the BNN
and compare argmax_a BNN(s,a) to argmax_a Q(s,a). An "equivalent" BNN achieves
100% match.

The equivalence is also exported as a PRP policy.out file — its rules describe
the BNN's decisions as Boolean decision-rules, exactly mirroring Q-table export.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, List, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

import brevitas.nn as qnn
from brevitas.quant import (
    SignedBinaryActPerTensorConst,
    SignedBinaryWeightPerTensorConst,
)


# Default quant objects — resolving at module load makes QuantLinear behave.
DEFAULT_WEIGHT_QUANT = SignedBinaryWeightPerTensorConst
DEFAULT_ACT_QUANT = SignedBinaryActPerTensorConst


# ---------------------------------------------------------------------------
# Binary network
# ---------------------------------------------------------------------------
@dataclass
class BNNConfig:
    in_dim: int = 4
    hidden_dims: Tuple[int, ...] = (16, 32)
    n_actions: int = 11
    weight_bit_width: int = 1
    activation_bit_width: int = 1
    learning_rate: float = 5e-3
    epochs: int = 600
    batch_size: int = 16
    seed: int = 0


class BinaryPolicyNet(nn.Module):
    """Quantised MLP used as the 'binary' surrogate of the Q-table."""

    def __init__(self, cfg: BNNConfig):
        super().__init__()
        self.cfg = cfg
        layers: List[nn.Module] = []

        prev = cfg.in_dim
        for i, h in enumerate(cfg.hidden_dims):
            layers.append(
                qnn.QuantLinear(
                    in_features=prev,
                    out_features=h,
                    bias=True,
                    weight_bit_width=cfg.weight_bit_width,
                    weight_quant=DEFAULT_WEIGHT_QUANT,
                    bias_bit_width=8,
                )
            )
            layers.append(qnn.QuantIdentity(
                bit_width=cfg.activation_bit_width,
                act_quant=DEFAULT_ACT_QUANT,
            ))
            prev = h

        # Output layer (binary weights, full-precision bias)
        layers.append(
            qnn.QuantLinear(
                in_features=prev,
                out_features=cfg.n_actions,
                bias=True,
                weight_bit_width=cfg.weight_bit_width,
                weight_quant=DEFAULT_WEIGHT_QUANT,
                bias_bit_width=8,
            )
        )
        self.layers = nn.ModuleList(layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = x
        for layer in self.layers:
            h = layer(h)
        return h

    # ------------------------------------------------------------------ utils
    @torch.no_grad()
    def predict_action(self, obs: np.ndarray) -> int:
        self.eval()
        x = torch.tensor(obs, dtype=torch.float32).unsqueeze(0)
        q = self.forward(x).squeeze(0).cpu().numpy()
        return int(np.argmax(q))

    @torch.no_grad()
    def q_table(self) -> np.ndarray:
        """Enumerate Q-values for all 16 binary states."""

        self.eval()
        rows = []
        for bits in product([0, 1], repeat=self.cfg.in_dim):
            x = torch.tensor(bits, dtype=torch.float32).unsqueeze(0)
            q = self.forward(x).squeeze(0).cpu().numpy()
            rows.append(q)
        return np.stack(rows, axis=0)

    @torch.no_grad()
    def greedy_table(self) -> List[Tuple[Tuple[int, ...], int]]:
        return [(bits, int(np.argmax(self.q_table()[i])))
                for i, bits in enumerate(product([0, 1], repeat=self.cfg.in_dim))]


# ---------------------------------------------------------------------------
# Training utilities
# ---------------------------------------------------------------------------
def build_bnn_targets_from_qtable(q_table: np.ndarray, *, mode: str = "q") -> np.ndarray:
    """Build training targets from a converged Q-table.

    mode="q":     target = q_table[i]   (regression on Q-values).
    mode="ce":    target = one-hot of argmax Q-table (cross-entropy).
    """

    if mode == "q":
        return q_table.astype(np.float32)
    if mode == "ce":
        idx = np.argmax(q_table, axis=1)
        out = np.zeros_like(q_table, dtype=np.float32)
        out[np.arange(len(q_table)), idx] = 1.0
        return out
    raise ValueError(f"Unknown mode: {mode}")


def train_bnn_from_qtable(
    q_table: np.ndarray,
    cfg: BNNConfig | None = None,
    *,
    mode: str = "q",
    log_every: int = 100,
    verbose: bool = False,
) -> Tuple[BinaryPolicyNet, List[float]]:
    """Train BNN with Q-table as supervision.

    The dataset has only 16 entries (one per binary state); we train
    "epochs" epochs of full-batch gradient descent.
    """

    cfg = cfg or BNNConfig(n_actions=q_table.shape[1])
    torch.manual_seed(cfg.seed)
    np.random.seed(cfg.seed)

    # Build inputs: 16 binary state vectors
    states = np.array(list(product([0, 1], repeat=cfg.in_dim)), dtype=np.float32)
    x = torch.tensor(states)
    y = torch.tensor(build_bnn_targets_from_qtable(q_table, mode=mode))

    model = BinaryPolicyNet(cfg)
    optim = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)

    losses: List[float] = []
    for ep in range(cfg.epochs):
        model.train()
        optim.zero_grad()
        # We feed all 16 samples every step (full-batch).
        out = model(x)
        if mode == "q":
            loss = F.mse_loss(out, y)
        else:
            loss = F.cross_entropy(out, y.argmax(dim=1))
        loss.backward()
        optim.step()
        losses.append(loss.item())
        if verbose and (ep == 0 or (ep + 1) % log_every == 0 or ep == cfg.epochs - 1):
            print(f"  BNN epoch {ep+1:4d}  loss={loss.item():.4f}")

    return model, losses


# ---------------------------------------------------------------------------
# Truth-table inspection: enumerate all 2^in_dim inputs -> argmax output.
# ---------------------------------------------------------------------------
def bnn_truth_table(model: BinaryPolicyNet) -> List[Tuple[Tuple[int, ...], int, int]]:
    """Return [(state_bits, bnn_argmax, bnn_predict_action)].

    Both ints come from the BNN — to compare against a ground-truth Q-table,
    use `verify_equivalence(model, q_table)` from `equivalence.py`.
    """

    rows = []
    qt = model.q_table()
    for i, bits in enumerate(product([0, 1], repeat=model.cfg.in_dim)):
        bnn_act = int(np.argmax(qt[i]))
        rows.append((bits, bnn_act, model.predict_action(np.array(bits, dtype=np.float32))))
    return rows


__all__ = ["BinaryPolicyNet", "BNNConfig", "train_bnn_from_qtable", "bnn_truth_table", "build_bnn_targets_from_qtable"]
