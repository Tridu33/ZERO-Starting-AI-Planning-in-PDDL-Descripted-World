"""Equivalence verifier: compare BNN argmax against ground-truth Q-table.

Verifies that the BinaryPolicyNet's argmax over the action dimension equals
the argmax of the supplied (converged) Q-table, for every 4-bit binary state.

Returns a structured verdict:

    {
        "match": bool,
        "n_match": int, "n_total": int,
        "mismatches": List[Tuple[bits, q_action, bnn_action, q_values, bnn_values]],
        "per_state": List[Dict],
    }
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, List, Tuple

import numpy as np

from .bnn import BinaryPolicyNet


# Mapping from int → "varX:Y" PRP variable encoding.
def var_token(i: int, val: int) -> str:
    # The variable ordering in PRP is var0, var1, var2, var3 representing
    # [BlocksCleared, H, VGoal, VStart]. We keep the same encoding throughout
    # the project.
    return f"var{i}:{val}"


# Abstract action names — index matches the BNN / Q-table column.
ABSTRACT_ACTIONS: Tuple[str, ...] = (
    "virtual_source_act",
    "goal",
    "putdown",
    "unstack",
)


def q_table_argmax(q_table: np.ndarray) -> Dict[Tuple[int, ...], int]:
    out: Dict[Tuple[int, ...], int] = {}
    for i, bits in enumerate(product([0, 1], repeat=q_table.shape[1] and 4 or 4)):
        # We expect q_table shape (16, n_actions); infer nS = 16.
        if q_table.ndim != 2 or q_table.shape[0] != 16:
            raise ValueError(f"Unexpected q_table shape {q_table.shape}")
        out[bits] = int(np.argmax(q_table[i]))
    return out


@dataclass
class EquivalenceResult:
    match: bool
    n_match: int
    n_total: int
    mismatches: List[Dict]
    per_state: List[Dict]

    def __str__(self) -> str:
        s = f"Equivalence: {self.n_match}/{self.n_total} states match"
        if self.mismatches:
            s += f" — {len(self.mismatches)} mismatches"
        return s


def verify_equivalence(
    bnn: BinaryPolicyNet,
    q_table: np.ndarray,
    *,
    expected_argmax: Dict[Tuple[int, ...], int] | None = None,
) -> EquivalenceResult:
    """Compare argmax_q(s) vs argmax_BNN(s) for all 16 binary states."""

    bnn_q = bnn.q_table()  # (16, n_actions)
    if bnn_q.shape != q_table.shape:
        raise ValueError(
            f"Q-table shape mismatch: bnn={bnn_q.shape} vs reference={q_table.shape}"
        )

    if expected_argmax is None:
        expected_argmax = q_table_argmax(q_table)

    n_match = 0
    per_state: List[Dict] = []
    mismatches: List[Dict] = []
    n_total = 16
    for idx, bits in enumerate(product([0, 1], repeat=4)):
        q_argmax = expected_argmax[bits]
        bnn_argmax = int(np.argmax(bnn_q[idx]))
        is_match = (q_argmax == bnn_argmax)
        if is_match:
            n_match += 1
        per_state.append(
            {
                "bits": bits,
                "q_argmax": q_argmax,
                "q_value_at_argmax": float(q_table[idx][q_argmax]),
                "bnn_argmax": bnn_argmax,
                "bnn_value_at_argmax": float(bnn_q[idx][bnn_argmax]),
                "match": bool(is_match),
            }
        )
        if not is_match:
            mismatches.append(
                {
                    "bits": bits,
                    "q_argmax": q_argmax,
                    "q_argmax_label": ABSTRACT_ACTIONS[q_argmax],
                    "bnn_argmax": bnn_argmax,
                    "bnn_argmax_label": ABSTRACT_ACTIONS[bnn_argmax],
                    "q_values": q_table[idx].tolist(),
                    "bnn_values": bnn_q[idx].tolist(),
                }
            )

    return EquivalenceResult(
        match=(n_match == n_total),
        n_match=n_match,
        n_total=n_total,
        mismatches=mismatches,
        per_state=per_state,
    )


__all__ = [
    "EquivalenceResult",
    "verify_equivalence",
    "ABSTRACT_ACTIONS",
    "var_token",
]
