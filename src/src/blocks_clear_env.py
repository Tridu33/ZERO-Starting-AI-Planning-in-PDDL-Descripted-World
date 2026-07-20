"""BlocksClearEnv - 基于 PDDL state-machine 的 Gym 环境。

目标：在 uv 创建的 Python 环境中模拟 blocks_clear 域与其初始问题，
       暴露 obs 为 4 维布尔向量 [BlocksCleared, H, VGoal, VStart]，
       暴露 action 为全部 ground 后的动作 + 两个特殊动作（virtual_source, goal）。

依赖说明：
    - 不依赖第三方 PDDL parser；本域只涉及 3 个对象 (A, x, y)，
      完全采用轻量级 Python 集合存状态并执行 STRIPS-effect。
    - 使用 gymnasium.spaces 暴露 obs/action 空间。
    - 派生谓词 (BlocksCleared, H) 与人类策略一致：
        BlocksCleared ≡ clear(A)
        H ≡ ∃x. holding(x)
        VGoal ≡ BlocksCleared       （当 clear(A) 达成 = 目标完成）
        VStart  ≡ 仅在 reset() 后第一次 step 之前的初始状态
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from itertools import product
from typing import Dict, FrozenSet, List, Optional, Sequence, Tuple

import gymnasium as gym
import numpy as np
from gymnasium import spaces


# ---------------------------------------------------------------------------
# PDDL state utilities
# ---------------------------------------------------------------------------
GroundPredicate = Tuple[str, ...]   # ('on', 'A', 'B'); length 0 = proposition
State = FrozenSet[GroundPredicate]


def _pred(name: str, *args: str) -> GroundPredicate:
    return (name,) + tuple(args)


def _state_to_set(s: State) -> set:
    return {p for p in s}


# ---------------------------------------------------------------------------
# Domain data-classes (parsed from PDDL: domain + problem)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class PDDLOperator:
    """STRIPS operator, ground-indexed.

    pre: set of GroundPredicate required to fire.
    add: set of GroundPredicate added by the effect.
    del_: set of GroundPredicate removed by the effect.
    """

    name: str
    args: Tuple[str, ...]
    pre: FrozenSet[GroundPredicate]
    add: FrozenSet[GroundPredicate]
    del_: FrozenSet[GroundPredicate]

    def is_applicable(self, state: State) -> bool:
        return self.pre.issubset(state)

    def apply(self, state: State) -> State:
        return frozenset((state - self.del_) | self.add)


@dataclass(frozen=True)
class VirtualAction:
    """Pseudo-action for VStart (no pre) / Goal (no pre) markers in PRP."""

    name: str

    def is_applicable(self, state: State) -> bool:
        return True

    def apply(self, state: State) -> State:
        return state


# ---------------------------------------------------------------------------
# Grounding for the blocks_clear domain (hard-coded; see README.md)
# ---------------------------------------------------------------------------
DOMAIN_OBJECTS: Tuple[str, ...] = ("A", "x", "y")
DERIVED_PREDICATES: Tuple[str, ...] = ("BlocksCleared", "H", "VStart", "VGoal")


def grounding_actions() -> List[PDDLOperator]:
    """Return all grounded STRIPS operators for the blocks_clear domain.

    Domain actions (after commenting-out pickup/stack):
        :action putdown
            :parameters (?x - BlockType)
            :precondition (holding ?x)
            :effect (clear ?x) (arm_empty) (on_table ?x) (not (holding ?x))

        :action unstack
            :parameters (?x ?y - BlockType)
            :precondition (on ?x ?y) (clear ?x) (arm_empty)
            :effect (holding ?x) (clear ?y)
                    (not (on ?x ?y)) (not (clear ?x)) (not (arm_empty))
    """

    objs = DOMAIN_OBJECTS
    ops: List[PDDLOperator] = []

    # ---- putdown(?x) ----
    for x in objs:
        ops.append(
            PDDLOperator(
                name="putdown",
                args=(x,),
                pre=frozenset({_pred("holding", x)}),
                add=frozenset(
                    {
                        _pred("clear", x),
                        _pred("arm_empty"),
                        _pred("on_table", x),
                    }
                ),
                del_=frozenset({_pred("holding", x)}),
            )
        )

    # ---- unstack(?x, ?y) ----
    # 全部组合; STRIPS pre-check 过滤无效 grounding。
    for x, y in product(objs, objs):
        if x == y:
            continue  # self-loop 解是不合语义的
        ops.append(
            PDDLOperator(
                name="unstack",
                args=(x, y),
                pre=frozenset(
                    {
                        _pred("on", x, y),
                        _pred("clear", x),
                        _pred("arm_empty"),
                    }
                ),
                add=frozenset(
                    {
                        _pred("holding", x),
                        _pred("clear", y),
                    }
                ),
                del_=frozenset(
                    {
                        _pred("on", x, y),
                        _pred("clear", x),
                        _pred("arm_empty"),
                    }
                ),
            )
        )

    return ops


# ---------------------------------------------------------------------------
# Initial problem: matches domains/blocks_clear/low_blocks_clear_p1.pddl
#   (:init (on_table A) (arm_empty) (on x A) (on y x) (clear y))
#   (:goal (clear A))
# ---------------------------------------------------------------------------
def initial_state() -> State:
    return frozenset(
        {
            _pred("on_table", "A"),
            _pred("arm_empty"),
            _pred("on", "x", "A"),
            _pred("on", "y", "x"),
            _pred("clear", "y"),
        }
    )


def goal_reached(state: State) -> bool:
    return _pred("clear", "A") in state


# ---------------------------------------------------------------------------
# Feature vector: [BlocksCleared, H, VGoal, VStart]
# ---------------------------------------------------------------------------
FEATURE_NAMES: Tuple[str, ...] = ("BlocksCleared", "H", "VGoal", "VStart")


def features_from_state(state: State, *, vstart_active: bool) -> np.ndarray:
    """Return a 4-vector of 0/1 float features.

    vstart_active: True only at the FIRST state after reset() (until the agent
    takes its first action).  We model it via the environment flag rather than a
    state predicate because VStart is a virtual marker used by PRP.
    """

    blockscleared = 1.0 if _pred("clear", "A") in state else 0.0
    h = 1.0 if any(p[0] == "holding" for p in state) else 0.0
    vgoal = 1.0 if _pred("clear", "A") in state else 0.0  # blockscleared ≡ goal
    vstart = 1.0 if vstart_active else 0.0
    return np.array([blockscleared, h, vgoal, vstart], dtype=np.float32)


# ---------------------------------------------------------------------------
# Gym environment
# ---------------------------------------------------------------------------
class BlocksClearEnv(gym.Env):
    """Blocks-clear Gymnasium environment.

    Observation:
        4-D float32 vector: [BlocksCleared, H, VGoal, VStart]

    Action:
        Discrete(N) where N = #grounded_ops + 2 (virtual_source_act + goal).
        The action space is FIXED for the entire training run to keep the
        DQN tabular mapping consistent.

    Reward:
        Default shaping: 0 except:
            +1  on transition where BlocksCleared flips 0->1.
            -0.1 per invalid/illegal action (rejected, agent stays in place).
        Done = True when goal_reached(state).
    """

    metadata = {"render_modes": []}

    # 0 / 1 are reserved for virtual_start / goal.
    VIRTUAL_START_IDX = 0
    GOAL_IDX = 1

    def __init__(
        self,
        operators: Optional[Sequence[PDDLOperator]] = None,
        reward_goal: float = 1.0,
        reward_invalid: float = -0.1,
        reward_step: float = 0.0,
        max_steps: int = 64,
    ) -> None:
        super().__init__()
        self.ops: List[PDDLOperator] = list(operators) if operators else grounding_actions()
        self.action_labels: List[str] = self._build_action_labels(self.ops)
        self.n_actions: int = len(self.action_labels)
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(4,), dtype=np.float32)
        self.action_space = spaces.Discrete(self.n_actions)
        self.reward_goal = reward_goal
        self.reward_invalid = reward_invalid
        self.reward_step = reward_step
        self.max_steps = max_steps

        # Internal state
        self._state: State = frozenset()
        self._vstart_active: bool = False
        self._steps: int = 0

    # ------------------------------------------------------------------ utils
    @staticmethod
    def _build_action_labels(ops: Sequence[PDDLOperator]) -> List[str]:
        labels = ["virtual_source_act", "goal"]
        for op in ops:
            labels.append(op.name + "_" + "_".join(op.args))
        return labels

    def action_name(self, idx: int) -> str:
        return self.action_labels[idx]

    # ------------------------------------------------------------------ reset
    def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None):
        super().reset(seed=seed)
        self._state = initial_state()
        self._vstart_active = True
        self._steps = 0
        obs = features_from_state(self._state, vstart_active=self._vstart_active)
        return obs, {}

    # ------------------------------------------------------------------ step
    def step(self, action: int):
        self._steps += 1

        # First step after reset clears the VStart marker.
        is_first_real_action = self._vstart_active

        # Virtual start: only valid at the very beginning; no state change.
        if action == self.VIRTUAL_START_IDX:
            if not is_first_real_action:
                # Treating it as a no-op when not at start slightly penalises.
                obs = features_from_state(self._state, vstart_active=False)
                return obs, float(self.reward_invalid), False, False, {"info": "vstart_dummy"}
            self._vstart_active = False
            obs = features_from_state(self._state, vstart_active=False)
            return obs, 0.0, False, False, {"info": "vstart_fired"}

        # Goal: stop.
        if action == self.GOAL_IDX:
            obs = features_from_state(self._state, vstart_active=False)
            return obs, 0.0, True, False, {"info": "goal_action"}

        # Real STRIPS operators: index 2..N-1.
        op_idx = action - 2
        if op_idx < 0 or op_idx >= len(self.ops):
            obs = features_from_state(self._state, vstart_active=False)
            return obs, float(self.reward_invalid), False, False, {"info": "out_of_range"}

        op = self.ops[op_idx]
        if not op.is_applicable(self._state):
            obs = features_from_state(self._state, vstart_active=False)
            return obs, float(self.reward_invalid), False, False, {"info": "inapplicable"}

        old_blockscleared = _pred("clear", "A") in self._state
        new_state = op.apply(self._state)
        self._state = new_state
        self._vstart_active = False  # any real action clears VStart

        # Default step reward + possible goal-bonus.
        reward = float(self.reward_step)
        info = {"info": op.name, "args": op.args}
        if not old_blockscleared and (_pred("clear", "A") in self._state):
            reward += float(self.reward_goal)
            obs = features_from_state(self._state, vstart_active=False)
            return obs, reward, True, False, {**info, "info": "goal_reached"}
        if self._steps >= self.max_steps:
            obs = features_from_state(self._state, vstart_active=False)
            return obs, reward, False, True, {**info, "info": "truncated"}
        obs = features_from_state(self._state, vstart_active=False)
        return obs, reward, False, False, info

    # ------------------------------------------------------------------ helpers
    def current_state(self) -> State:
        return self._state

    def applicable_indices(self, *, include_virtual: bool = True) -> List[int]:
        """Return all action indices applicable in the current state.

        By default (include_virtual=True) the VIRTUAL_START and GOAL indices are
        added only when the flag is actually meaningful — VIRTUAL_START when
        ``vstart_active``, GOAL when the goal predicate is satisfied. Pass
        include_virtual=False to restrict to STRIPS actions.
        """

        a: List[int] = []
        if include_virtual:
            if self._vstart_active:
                a.append(self.VIRTUAL_START_IDX)
            if goal_reached(self._state):
                a.append(self.GOAL_IDX)
        for i, op in enumerate(self.ops):
            if op.is_applicable(self._state):
                a.append(i + 2)
        return a


# ---------------------------------------------------------------------------
# State enumeration utility
# ---------------------------------------------------------------------------
def enumerate_all_states() -> Dict[State, np.ndarray]:
    """Enumerate a reasonable state-space slice for the blocks_clear domain.

    Because the state-space is finite and small (4 derived booleans), this
    helper iterates the 16 boolean combinations and, for each, finds a
    representative underlying PDDL state from a closed-world simulator.
    Returns a dict mapping the 4-vector -> the underlying state (for
    equivalence/regression purposes).
    """

    from .state_enumerator import all_reachable_states

    cache: Dict[State, np.ndarray] = {}
    for st in all_reachable_states():
        for vs in (True, False):
            feat = features_from_state(st, vstart_active=vs)
            cache.setdefault(tuple(feat.tolist()), (st, vs))
    return {k: v for k, v in cache.items()}


__all__ = [
    "BlocksClearEnv",
    "DOMAIN_OBJECTS",
    "DERIVED_PREDICATES",
    "FEATURE_NAMES",
    "PDDLOperator",
    "VirtualAction",
    "features_from_state",
    "grounding_actions",
    "initial_state",
    "goal_reached",
]
