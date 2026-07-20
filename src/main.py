"""Main entry point for the Policy4FONDRL2BNN pipeline.

Stages
------
1. Build the Blocks_clear Gym environment with PDDL state-machine.
2. Train a PyG relational feature encoder (PDDL state -> 4-bit vector).
3. Train a DQN over the 4-bit MDP and verify Q-table quality.
4. Solve the abstract MDP via value-iteration to obtain the ground-truth
   Q-table (16 x 4) — this is the supervisor for the Brevitas BNN.
5. Train the Brevitas BinaryPolicyNet with the Q-table as supervision.
6. Verify BNN equivalence against the Q-table on all 16 binary states.
7. Export policy to PRP-compatible human_policy.out and policy.out, in
   both blocks_clear solution directories.
8. Save all artifacts (Q-table snapshots, BNN weights, JSON summaries).

Run as:
    python main.py
or via:
    uv run python main.py

Outputs land in:
    policies/block_clear/                — PRP-compatible policy files
    artifacts/                           — training artefacts and logs
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List

import numpy as np
import torch

# Make `src` importable when run as `python main.py` from the project root.
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.blocks_clear_env import BlocksClearEnv
from src.feature_extractor import (
    RelationalFeatureEncoder,
    train_relational_encoder,
)
from src.mdp_solver import (
    ABSTRACT_ACTIONS,
    build_abstract_mdp,
    solve_abstract,
)
from src.dqn import DQNAgent, DQNConfig
from src.bnn import (
    BNNConfig,
    BinaryPolicyNet,
    train_bnn_from_qtable,
)
from src.equivalence import (
    ABSTRACT_ACTIONS,
    EquivalenceResult,
    verify_equivalence,
)
from src.policy_exporter import export_prp_policy


# ---------------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = ROOT
PROJECT_ROOT_STR = str(ROOT)
DOMAIN_DIR = ROOT / "domains" / "blocks_clear"
POLICY_DIR = ROOT / "policies" / "block_clear"
ARTIFACT_DIR = ROOT / "artifacts"
PRP_POLICY_DIR = Path("/tridu33/SAVG/PRP_planner-for-relevant-policies/solutionsByPRP")

for d in (POLICY_DIR, ARTIFACT_DIR, PRP_POLICY_DIR):
    d.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SEED = 0
GAMMA = 0.95
ENCODER_EPOCHS = 200
DQN_EPISODES = 500
BNN_HIDDEN = (32, 64, 32)
BNN_EPOCHS = 600
BNN_MODE = "ce"


# ---------------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------------
def stage1_environment():
    print("[stage 1] Building Blocks_clear Gym environment ...")
    env = BlocksClearEnv()
    obs, _ = env.reset()
    print(f"  initial obs = {obs.tolist()}  (var0=BlocksCleared, var1=H, var2=VGoal, var3=VStart)")
    print(f"  n_actions   = {env.n_actions}")
    print(f"  labels      = {env.action_labels}")
    return env


def stage2_feature_encoder(env: BlocksClearEnv):
    print()
    print("[stage 2] Training PyG relational feature encoder ...")
    encoder, losses = train_relational_encoder(
        epochs=ENCODER_EPOCHS,
        lr=5e-2,
        hidden_dim=16,
        n_layers=3,
        seed=SEED,
        verbose=False,
    )
    print(f"  losses[-1] = {losses[-1]:.4f}  (over {ENCODER_EPOCHS} epochs)")

    # Quick sanity check.
    from src.blocks_clear_env import initial_state
    pred = encoder.encode_state(initial_state(), vstart_active=True)
    print(f"  vstart-state prediction: {pred.tolist()}  (expected [0., 0., 0., 1.])")

    # Persist encoder weights.
    enc_path = ARTIFACT_DIR / "relational_encoder.pt"
    torch.save(encoder.state_dict(), enc_path)
    print(f"  saved encoder to {enc_path}")
    return encoder


def stage3_dqn(env: BlocksClearEnv):
    """Train DQN as an extra validation step (not the canonical Q-table)."""

    print()
    print("[stage 3] Training DQN (small MLP, 4 -> 32 -> 32 -> 11) ...")
    cfg = DQNConfig(
        n_episodes=DQN_EPISODES,
        learning_starts=128,
        batch_size=32,
        eps_decay_steps=300,
        target_sync_steps=50,
        seed=SEED,
        hidden=32,
    )
    agent = DQNAgent(env, env.n_actions, cfg)
    rewards = agent.train(log_every=100)
    print(f"  final 100-episode reward mean = {np.mean(rewards[-100:]):+.3f}")

    q = agent.q_table()
    print(f"  DQN Q-table shape: {q.shape}")
    print("  DQN greedy table on 4-bit states:")
    from itertools import product
    for bits in product([0, 1], repeat=4):
        a = int(np.argmax(q[bits[0] * 8 + bits[1] * 4 + bits[2] * 2 + bits[3]]))
        print(f"    {bits} -> {env.action_labels[a]}")
    return agent, rewards


def stage4_abstract_mdp(env: BlocksClearEnv):
    print()
    print("[stage 4] Solving abstract 16x4 MDP via value iteration ...")
    sol = solve_abstract(env, gamma=GAMMA)
    print(f"  converged in {sol.n_iterations} iterations")
    print(f"  Q-table shape: {sol.q_table.shape}")
    return sol


def stage5_bnn(sol):
    print()
    print("[stage 5] Training Brevitas BinaryPolicyNet with Q-table supervision ...")
    q = sol.q_table

    best_match = 0
    best: BinaryPolicyNet | None = None
    best_seed = SEED
    for seed in range(8):
        cfg = BNNConfig(
            n_actions=4,
            hidden_dims=BNN_HIDDEN,
            epochs=BNN_EPOCHS,
            learning_rate=2e-2,
            seed=seed,
        )
        bnn, _ = train_bnn_from_qtable(q, cfg, mode=BNN_MODE, verbose=False)
        res = verify_equivalence(bnn, q)
        print(f"  seed={seed:2d}  match = {res.n_match}/16")
        if res.n_match > best_match:
            best_match = res.n_match
            best = bnn
            best_seed = seed

    print()
    print(f"  best BNN: seed={best_seed}, match={best_match}/16")

    # Save the winning BNN weights.
    bnn_path = ARTIFACT_DIR / "bnn_best.pt"
    torch.save(
        {
            "model_state": best.state_dict(),
            "config": best.cfg.__dict__,
            "match": best_match,
            "seed": best_seed,
        },
        bnn_path,
    )
    print(f"  saved BNN to {bnn_path}")
    return best


def stage6_equivalence(bnn: BinaryPolicyNet, sol):
    print()
    print("[stage 6] Verifying BNN ↔ Q-table equivalence ...")
    result = verify_equivalence(bnn, sol.q_table)
    print(f"  {result}")
    if result.mismatches:
        print("  mismatches:")
        for m in result.mismatches:
            print(f"    bits={m['bits']} q={m['q_argmax_label']} bnn={m['bnn_argmax_label']}")
    return result


def stage7_export(sol):
    print()
    print("[stage 7] Exporting PRP-compatible policy files ...")
    artifacts = export_prp_policy(
        greedy_table=sol.greedy_table,
        abstract_actions=ABSTRACT_ACTIONS,
        output_dir=str(POLICY_DIR),
        domain_name="fond_blocks_clear",
    )

    # Mirror into PRP_planner-for-relevant-policies/solutionsByPRP/ for the
    # user's pipeline.
    mirror_dir = PRP_POLICY_DIR
    mirror_dir.mkdir(parents=True, exist_ok=True)
    mirror_paths = []
    for src in (artifacts.policy_out_path, artifacts.human_policy_out_path):
        dst = mirror_dir / Path(src).name
        with open(src, "r") as fr, open(dst, "w") as fw:
            fw.write(fr.read())
        mirror_paths.append(str(dst))

    print(f"  wrote {artifacts.num_rules} rules to:")
    print(f"    {artifacts.policy_out_path}")
    print(f"    {artifacts.human_policy_out_path}")
    print(f"  mirror:")
    for p in mirror_paths:
        print(f"    {p}")
    return artifacts


def stage8_summary(env, sol, bnn: BinaryPolicyNet, result: EquivalenceResult, artifacts, agent, dqn_rewards):
    """Persist a machine-readable summary alongside the PRP files."""

    from itertools import product

    def idx(bits):
        return bits[0] * 8 + bits[1] * 4 + bits[2] * 2 + bits[3]

    summary = {
        "domain": "blocks_clear",
        "n_states": 16,
        "n_actions_grounded": env.n_actions,
        "n_actions_abstract": 4,
        "abstract_actions": list(ABSTRACT_ACTIONS),
        "gamma": GAMMA,
        "value_iteration_iterations": sol.n_iterations,
        "equivalence": {
            "match": result.match,
            "n_match": result.n_match,
            "n_total": result.n_total,
            "mismatches": result.mismatches,
        },
        "bnn": {
            "hidden_dims": list(BNN_HIDDEN),
            "epochs": BNN_EPOCHS,
            "mode": BNN_MODE,
        },
        "dqn": {
            "episodes": DQN_EPISODES,
            "reward_mean_last100": float(np.mean(dqn_rewards[-100:])) if dqn_rewards else 0.0,
        },
        "policies": {
            "policy_out": artifacts.policy_out_path,
            "human_policy_out": artifacts.human_policy_out_path,
        },
        "q_table_dense_argmax": {
            f"{bits}": int(np.argmax(sol.q_table[idx(bits)]))
            for bits in product([0, 1], repeat=4)
        },
        "q_table": sol.q_table.tolist(),
        "bnn_q_table": bnn.q_table().tolist(),
    }
    out = ARTIFACT_DIR / "summary.json"
    with open(out, "w") as f:
        json.dump(summary, f, indent=2)
    print()
    print(f"[stage 8] Summary written to {out}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> None:
    t0 = time.time()
    env = stage1_environment()
    encoder = stage2_feature_encoder(env)
    agent, dqn_rewards = stage3_dqn(env)
    sol = stage4_abstract_mdp(env)
    bnn = stage5_bnn(sol)
    res = stage6_equivalence(bnn, sol)
    artifacts = stage7_export(sol)
    stage8_summary(env, sol, bnn, res, artifacts, agent, dqn_rewards)
    elapsed = time.time() - t0
    print(f"\nTotal runtime: {elapsed:.2f}s")


if __name__ == "__main__":
    main()
