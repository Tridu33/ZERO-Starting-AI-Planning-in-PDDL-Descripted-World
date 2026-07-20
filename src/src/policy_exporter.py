"""Export the blocks_clear policy to PRP-compatible format.

Two formats are supported:

1. policy.out — variable-encoded rules in PRP notation:
       If holds: var3:1 var0:1 var1:1 var2:1
       Execute: 0_unstack_1_7  / SC / d=1

   In PRP, the variable index ordering is (var0, var1, var2, var3) ≡
   (BlocksCleared, H, VGoal, VStart). And crucially, var_i:0 means the
   predicate IS HELD (TRUE), while var_i:1 means the predicate IS NOT HELD
   (FALSE).  We must therefore INVERT each bit when exporting.

2. human_policy.out — semantic Pddl-aware format used by the existing
   projects under PRP_planner-for-relevant-policies/solutionsByPRP/.
   The variable → predicate mapping block is prepended, followed by
   `Policy:` and `FSAP:` sections using natural-language predicates.

Both formats use one line per decision, sorted for deterministic output.
The depth column ('d') in PRP convention is omitted (set to 0) because
this project focuses on policy equivalence rather than planning depth.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from itertools import product
from typing import Dict, List, Tuple

import numpy as np


# Variable i -> predicate. Mapping taken from
# PRP_planner-for-relevant-policies/solutionsByPRP/fond_blocks_clear_human_policy.out
VAR_NAMES: Tuple[str, ...] = (
    "BlocksCleared",   # var0
    "H",                # var1
    "VGoal",            # var2
    "VStart",           # var3
)


def bits_to_prp_conditions(bits: Tuple[int, ...]) -> str:
    """Convert a 4-bit feature tuple to the PRP "var_i:j" line.

    PRP convention: var_i:0 means PREDICATE i IS TRUE (i.e. our bits[i] = 1).
    So we flip the bit before emitting.
    """

    parts: List[str] = []
    for i, b in enumerate(bits):
        # Flip: bits[i]=1 (predicate true) -> var_i:0
        flipped = 1 - int(b)
        parts.append(f"var{i}:{flipped}")
    return " ".join(parts)


def bits_to_human_conditions(bits: Tuple[int, ...]) -> str:
    """Convert 4-bit tuple to "not(p_i)/p_i/p_i/..." style conditional.

    Returns a slash-separated string suitable for the human_policy.out format.
    """

    parts: List[str] = []
    for i, b in enumerate(bits):
        if int(b) == 1:
            parts.append(VAR_NAMES[i].lower())
        else:
            parts.append(f"not({VAR_NAMES[i].lower()}())")
    return "/".join(parts)


def action_to_prp_label(action_idx: int, abstract_actions: Tuple[str, ...]) -> str:
    """Map an abstract-action index to the PRP action label.

    The exact label uses PRP's grounded-action naming scheme (numeric prefix):
        0_unstack_1_7, 1_putdown_0, 8_virtual_source_act_0
    """

    name = abstract_actions[action_idx]
    if name == "virtual_source_act":
        return "8_virtual_source_act_0"
    if name == "goal":
        return "goal"
    if name == "putdown":
        return "1_putdown_0"
    if name == "unstack":
        return "0_unstack_1_7"
    return f"{action_idx}_{name}"


def depth_for_bits(bits: Tuple[int, ...]) -> int:
    """Heuristic depth: 0 for goal-ish states, otherwise 2."""

    bc, h, vg, vs = bits
    if vg:
        return 0
    if vs:
        return 2
    return 1 if (bc and h) else 1


# ---------------------------------------------------------------------------
# Top-level export
# ---------------------------------------------------------------------------
@dataclass
class ExportArtifacts:
    policy_out_path: str
    human_policy_out_path: str
    num_rules: int


def export_prp_policy(
    greedy_table: Dict[Tuple[int, ...], int],
    abstract_actions: Tuple[str, ...],
    output_dir: str,
    *,
    domain_name: str = "fond_blocks_clear",
) -> ExportArtifacts:
    """Write both policy.out and human_policy.out files under ``output_dir``."""

    os.makedirs(output_dir, exist_ok=True)
    policy_path = os.path.join(output_dir, f"{domain_name}_policy.out")
    human_path = os.path.join(output_dir, f"{domain_name}_human_policy.out")

    rules = []
    for bits in product([0, 1], repeat=4):
        rules.append((bits, greedy_table[bits]))
    rules.sort(key=lambda r: r[0])

    # ----- policy.out -----
    with open(policy_path, "w") as f:
        f.write("\n")
        for bits, a in rules:
            cond = bits_to_prp_conditions(bits)
            label = action_to_prp_label(a, abstract_actions)
            depth = depth_for_bits(bits)
            f.write(f"If holds: {cond}\n")
            f.write(f"Execute: {label} / SC / d={depth}\n")
        f.write("\n")

    # ----- human_policy.out -----
    with open(human_path, "w") as f:
        f.write("Mapping:\n\n")
        # Variable -> predicate sections
        # PRP convention: var_i:0 <-> PREDICATE (held); var_i:1 <-> not(PREDICATE)
        for i, var in enumerate(VAR_NAMES):
            pred_lower = var.lower()
            f.write(f"  var{i}:0\t<-> \t {pred_lower}()\n")
            f.write(f"  var{i}:1\t<-> \t not({pred_lower}())\n")
            f.write("\n")

        f.write("Policy:\n\n")
        for bits, a in rules:
            cond = bits_to_human_conditions(bits)
            label = action_to_prp_label(a, abstract_actions)
            depth = depth_for_bits(bits)
            f.write(f"If holds: {cond}\n")
            f.write(f"Execute: {label}  / SC / d={depth}\n")
            f.write("\n")

        f.write("FSAP:\n\n")

    return ExportArtifacts(
        policy_out_path=policy_path,
        human_policy_out_path=human_path,
        num_rules=len(rules),
    )


__all__ = [
    "VAR_NAMES",
    "action_to_prp_label",
    "bits_to_human_conditions",
    "bits_to_prp_conditions",
    "depth_for_bits",
    "export_prp_policy",
    "ExportArtifacts",
]
