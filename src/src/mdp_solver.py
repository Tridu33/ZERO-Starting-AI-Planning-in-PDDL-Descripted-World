"""Abstract MDP solver over the 4-feature space with abstract actions.

The 4-feature abstraction collapses multiple grounded STRIPS actions.  We
follow the human convention:

    abstract actions:  "virtual_source_act", "goal",
                       "putdown", "unstack"

This makes the policy compact and matches PRP's "If holds: ..." rules.  The
grounding of each abstract action is decided at execution time — for the
export we keep the abstract labels.

The transition T(s, a_abstract) is computed over the *reachable* underlying
PDDL state space:
- For abstract "virtual_source_act": clears VStart.  Always available at vstart.
- For abstract "goal": available only when clear(A) holds.
- For abstract "putdown": takes the held block to the table and releases the
  arm.  Available iff H is true.
- For abstract "unstack": unstack any pickable block from its support.
  Available iff arm_empty AND some block is clear AND some block has
  another block on it.  The lifted effect is a state where H is true and
  one block became clear — we map it to the feature vector using a
  conservative abstraction.

This module emits a *deterministic, compact* 16 × 4 Q-table suitable for
BNN distillation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, List, Tuple

import numpy as np

from .blocks_clear_env import (
    BlocksClearEnv,
    DOMAIN_OBJECTS,
    State,
    features_from_state,
    goal_reached,
    initial_state,
)

# Avoid runtime circular import – alias here.
GoalPredicate_v0 = ("clear", "A")


ABSTRACT_ACTIONS: Tuple[str, ...] = ("virtual_source_act", "goal", "putdown", "unstack")


@dataclass
class AbstractMDP:
    nS: int = 16
    nA: int = 4
    # filled by build()
    transitions: np.ndarray = None     # (nS, nA, 3): [next_state, reward, done]
    abstract_action_for_state: Dict[Tuple[int, ...], int] = None

    def __post_init__(self):
        if self.transitions is None:
            self.transitions = np.zeros((self.nS, self.nA, 3), dtype=np.float32)
        if self.abstract_action_for_state is None:
            self.abstract_action_for_state = {}

    # ------------------------------------------------------------------ utils
    @staticmethod
    def bits_to_idx(bits: Tuple[int, ...]) -> int:
        return bits[0] * 8 + bits[1] * 4 + bits[2] * 2 + bits[3]

    @staticmethod
    def idx_to_bits(idx: int) -> Tuple[int, ...]:
        return (
            (idx >> 3) & 1,
            (idx >> 2) & 1,
            (idx >> 1) & 1,
            (idx) & 1,
        )


# ---------------------------------------------------------------------------
# Build the abstract MDP transitions by enumerating reachable PDDL states
# and lifting each transition to its corresponding feature vector.
# ---------------------------------------------------------------------------
def build_abstract_mdp(env: BlocksClearEnv) -> AbstractMDP:
    """Construct the 16x4 abstract MDP by exploring the underlying PDDL
    reachable graph.
    """

    from .state_enumerator import all_reachable_states

    mdp = AbstractMDP()

    # Map each reachable PDDL state to its feature bits.
    # Multiple PDDL states may share bits; we keep a representative one.
    bits_to_states: Dict[Tuple[int, ...], List[State]] = {}
    for st in all_reachable_states():
        bits = tuple(int(round(float(x))) for x in features_from_state(st, vstart_active=False))
        bits_to_states.setdefault(bits, []).append(st)

    # Helper: lift next PDDL state -> next bits.
    def _lift(st: State) -> Tuple[int, ...]:
        return tuple(int(round(float(x))) for x in features_from_state(st, vstart_active=False))

    # Helper: best-effort "abstract putdown" - applies the held block to be
    # on_table again with arm_empty.  Tries each grounded putdown; uses the
    # first applicable.
    def _abstract_putdown(st: State) -> State | None:
        for op in env.ops:
            if op.name == "putdown" and op.is_applicable(st):
                return op.apply(st)
        return None

    # Helper: "abstract unstack" - tries each grounded unstack; uses the
    # first applicable (typically unstack(y, x) at the initial state).
    def _abstract_unstack(st: State) -> State | None:
        for op in env.ops:
            if op.name == "unstack" and op.is_applicable(st):
                return op.apply(st)
        return None

    # Now build the 16x4 transitions table.  For each 4-bit vector we use a
    # representative PDDL state if available; otherwise we fall back to the
    # conservative interpretation.
    for i, bits in enumerate(product([0, 1], repeat=4)):
        bc, h, vg, vs = bits
        # ── 0: virtual_source_act ─────────────────────────────────────────
        if vs == 1:
            next_bits = (bc, h, vg, 0)
            rwd = 0.0
            done = bool(bc == 1)  # in the rare case where initial is goal
        else:
            # Illegal in non-vstart: stay + penalty.
            next_bits = bits
            rwd = env.reward_invalid
            done = False
        mdp.transitions[i, 0] = AbstractMDP.bits_to_idx(next_bits), rwd, float(done)

        # ── 1: goal ───────────────────────────────────────────────────────
        if vg == 1 or bc == 1:
            next_bits = bits
            rwd = 0.0
            done = True
        else:
            next_bits = bits
            rwd = env.reward_invalid
            done = False
        mdp.transitions[i, 1] = AbstractMDP.bits_to_idx(next_bits), rwd, float(done)

        # ── 2: putdown ────────────────────────────────────────────────────
        # Available when h=1.  Try lifting via the representative state.
        rep_states = bits_to_states.get(bits, [])
        next_state = None
        for st in rep_states:
            next_state = _abstract_putdown(st)
            if next_state is not None:
                break

        if h == 1 and next_state is not None:
            next_bits_after = _lift(next_state)
            # Mark BlocksCleared if the lifted state implies it (e.g., we
            # somehow make A clear via downstream effects — for our domain
            # putdown never clears A directly; clear(A) is only flipped by
            # unstack(x, A).  Still, carry the state forward transparently).
            goal_hit = bool(goal_reached(next_state))
            rwd = env.reward_goal if goal_hit else 0.0
            done = goal_hit
            mdp.transitions[i, 2] = AbstractMDP.bits_to_idx(next_bits_after), rwd, float(done)
        else:
            mdp.transitions[i, 2] = i, env.reward_invalid, 0.0

        # ── 3: unstack ────────────────────────────────────────────────────
        next_state = None
        for st in rep_states:
            next_state = _abstract_unstack(st)
            if next_state is not None:
                break
        if h == 0 and next_state is not None:
            next_bits_after = _lift(next_state)
            # The key question: did this unstack clear(A)?
            goal_hit = bool(goal_reached(next_state))
            rwd = env.reward_goal if goal_hit else 0.0
            done = goal_hit
            mdp.transitions[i, 3] = AbstractMDP.bits_to_idx(next_bits_after), rwd, float(done)
        else:
            mdp.transitions[i, 3] = i, env.reward_invalid, 0.0

    # Determine the deterministic abstract action per state via exact solving
    # on the lifted (16, 4) MDP.
    return mdp


# ---------------------------------------------------------------------------
# Value iteration on the abstract MDP
# ---------------------------------------------------------------------------
@dataclass
class AbstractSolution:
    q_table: np.ndarray            # (16, 4)
    v_table: np.ndarray            # (16,)
    greedy_table: Dict[Tuple[int, ...], int]   # (bc, h, vg, vs) -> action_index
    n_iterations: int


def solve_abstract(
    env: BlocksClearEnv,
    *,
    gamma: float = 0.95,
    max_iter: int = 1000,
    theta: float = 1e-10,
) -> AbstractSolution:
    mdp = build_abstract_mdp(env)
    nS, nA = mdp.nS, mdp.nA

    V = np.zeros(nS, dtype=np.float32)
    for it in range(max_iter):
        next_s = mdp.transitions[:, :, 0].astype(np.int64)
        reward = mdp.transitions[:, :, 1]
        done = mdp.transitions[:, :, 2]
        Q = reward + gamma * (1.0 - done) * V[next_s]
        V_new = Q.max(axis=1)
        delta = float(np.abs(V_new - V).max())
        V = V_new
        if delta < theta:
            break

    Q_final = Q
    greedy_table = {}
    for i in range(nS):
        bits = AbstractMDP.idx_to_bits(i)
        greedy_table[bits] = int(np.argmax(Q_final[i]))

    return AbstractSolution(
        q_table=Q_final,
        v_table=V,
        greedy_table=greedy_table,
        n_iterations=it + 1,
    )


__all__ = ["ABSTRACT_ACTIONS", "AbstractMDP", "AbstractSolution", "build_abstract_mdp", "solve_abstract"]
