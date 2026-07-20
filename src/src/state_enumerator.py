"""Reachable state enumeration for the blocks_clear domain.

The simplest way to obtain a closed-set of reachable states is BFS from the
initial state, using the grounded STRIPS operators defined in `blocks_clear_env`.
Because the domain has only 3 objects, the reachable state-space is small (single-
digit number of states), but we expose the machinery here in case the same code
is re-used for larger blocks-world variants.
"""

from __future__ import annotations

from collections import deque
from typing import Iterable, List, Set

from .blocks_clear_env import (
    PDDLOperator,
    State,
    goal_reached,
    grounding_actions,
    initial_state,
)


def all_reachable_states(operators: Iterable[PDDLOperator] | None = None) -> List[State]:
    """Breadth-first enumeration of all states reachable from the initial state."""

    ops = list(operators) if operators is not None else grounding_actions()
    init = initial_state()
    seen: Set[State] = {init}
    queue: deque[State] = deque([init])

    while queue:
        cur = queue.popleft()
        for op in ops:
            if op.is_applicable(cur):
                nxt = op.apply(cur)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)

    return sorted(seen, key=lambda s: sorted(map(str, s)))


def all_states_reachable_with_vstart(operators: Iterable[PDDLOperator] | None = None):
    """Like `all_reachable_states` but attaches the vstart flag (True only at init).

    Yields tuples of (State, vstart_active: bool).
    """

    ops = list(operators) if operators is not None else grounding_actions()
    init = initial_state()
    seen: Set[tuple] = {(init, True)}
    queue: deque = deque([(init, True)])
    while queue:
        cur, vs = queue.popleft()
        for op in ops:
            if op.is_applicable(cur):
                nxt = op.apply(cur)
                key = (nxt, False)  # any real action clears vstart
                if key not in seen:
                    seen.add(key)
                    queue.append(key)
    return [(s, v) for (s, v) in sorted(seen, key=lambda kv: sorted(map(str, kv[0])))]


def is_goal(state: State) -> bool:
    return goal_reached(state)


__all__ = ["all_reachable_states", "all_states_reachable_with_vstart", "is_goal"]
