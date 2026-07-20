"""End-to-end smoke tests for the Policy4FONDRL2BNN pipeline.

Run with `pytest` after installing pytest (optional).  All tests are also
importable under plain Python — see __main__ at the bottom.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.blocks_clear_env import (
    BlocksClearEnv,
    FEATURE_NAMES,
    features_from_state,
    initial_state,
    goal_reached,
)
from src.mdp_solver import solve_abstract, ABSTRACT_ACTIONS
from src.bnn import BNNConfig, train_bnn_from_qtable
from src.equivalence import verify_equivalence
from src.policy_exporter import export_prp_policy


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def test_environment_initial_state():
    env = BlocksClearEnv()
    obs, _ = env.reset()
    assert obs.shape == (4,)
    assert obs.tolist() == [0., 0., 0., 1.], "vstart state should be [BlocksCleared=0, H=0, VGoal=0, VStart=1]"
    print("  OK: env reset produces [0, 0, 0, 1]")


def test_environment_step():
    env = BlocksClearEnv()
    env.reset()
    # At initial state, the only applicable STRIPS op is unstack(y, x) (idx 10).
    obs, reward, done, trunc, info = env.step(10)  # unstack_y_x
    print(f"  unstack(y,x) -> {obs.tolist()}, reward={reward}, done={done}")
    assert done is False
    assert obs[1] == 1.0  # now holding (H=1)


def test_features_mapping():
    state = initial_state()
    feats = features_from_state(state, vstart_active=True)
    assert feats.tolist() == [0., 0., 0., 1.]


def test_abstract_solver_matches_human_policy():
    """The abstract policy should match the canonical human policy
    on the 4 reachable states from vstart.
    """

    env = BlocksClearEnv()
    sol = solve_abstract(env)
    # State (0,0,0,1) -> virtual_source_act (index 0)
    assert sol.greedy_table[(0, 0, 0, 1)] == 0, "vstart should fire virtual_source_act"
    # State (0,0,0,0) -> unstack (index 3)
    assert sol.greedy_table[(0, 0, 0, 0)] == 3, "post-vstart should unstack"
    # State (0,1,0,0) -> putdown (index 2)
    assert sol.greedy_table[(0, 1, 0, 0)] == 2, "after holding should putdown"
    # Any "purely goal-vgoal" state -> goal (index 1)
    for bits in [(0, 0, 1, 0), (0, 1, 1, 0), (1, 0, 1, 0)]:
        assert sol.greedy_table[bits] == 1, f"goal state {bits} should fire goal action"
    print("  OK: abstract policy matches canonical human-policy rules on reachable states")


def test_bnn_equivalence():
    env = BlocksClearEnv()
    sol = solve_abstract(env)
    bnn, _ = train_bnn_from_qtable(
        sol.q_table,
        BNNConfig(n_actions=4, hidden_dims=(32, 64, 32), epochs=600, learning_rate=2e-2, seed=0),
        mode="ce",
    )
    result = verify_equivalence(bnn, sol.q_table)
    assert result.match, f"BNN should match Q-table on all 16 states; mismatches={result.mismatches}"
    print(f"  OK: BNN matches Q-table on all 16 states (match={result.n_match}/{result.n_total})")


def test_policy_export(tmpdir=None):
    import tempfile, os
    env = BlocksClearEnv()
    sol = solve_abstract(env)
    with tempfile.TemporaryDirectory() as tmp:
        out = export_prp_policy(sol.greedy_table, ABSTRACT_ACTIONS, tmp)
        assert os.path.exists(out.policy_out_path)
        assert os.path.exists(out.human_policy_out_path)
        # Verify content
        with open(out.policy_out_path) as f:
            policy_text = f.read()
        assert "If holds: var" in policy_text
        assert "Execute:" in policy_text

        with open(out.human_policy_out_path) as f:
            human_text = f.read()
        assert "Mapping:" in human_text
        assert "Policy:" in human_text
        assert "FSAP:" in human_text
        assert "blockscleared()" in human_text
    print("  OK: policy export produces valid PRP files")


# ---------------------------------------------------------------------------
# Run all
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Running Policy4FONDRL2BNN end-to-end tests")
    print("=" * 60)
    print()
    print("[test] test_environment_initial_state")
    test_environment_initial_state()
    print("[test] test_environment_step")
    test_environment_step()
    print("[test] test_features_mapping")
    test_features_mapping()
    print("[test] test_abstract_solver_matches_human_policy")
    test_abstract_solver_matches_human_policy()
    print("[test] test_bnn_equivalence")
    test_bnn_equivalence()
    print("[test] test_policy_export")
    test_policy_export()
    print()
    print("All tests passed!")


if __name__ == "__main__":
    main()
