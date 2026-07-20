"""Relational feature extractor — PDDL state → 4-dim Boolean vector.

使用 PyTorch Geometric 把 PDDL 状态的关系结构表达成图, 然后用 GIN 风格
的 message-passing 网络 + MLP head 将其映射为给定的 4 个布尔谓词
[BlocksCleared, H, VGoal, VStart].

* 节点 (objects): 每个对象一个节点 (A, x, y)
* 节点特征: on_table(?x), clear(?x), holding(?x) → 3 维
* 边 (relations): on(?x, ?y) 作为 directed edge (x → y)
* 全局特征: arm_empty 加入 readout bias

训练目标: 用环境枚举器求出的 oracle 4 维向量作为监督, 训练模型完美逼近
这种关系编码 (并且其输出足以作为下游 DQN 的状态表示)。

注意: 真实跑训练时无需 PyG 也完全够用, 因为域对象数固定 (3); 但本模块
展示了如何把 PDDL → 关系图 → 4 维谓词向量接入 GNN, 满足用户提出的
"用 PyG 把 PDDL 状态的关系结构编码为 embedding" 要求。
"""

from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.data import Data, Batch
from torch_geometric.nn import GINConv, global_add_pool

from .blocks_clear_env import (
    DOMAIN_OBJECTS,
    FEATURE_NAMES,
    GroundPredicate,
    State,
    features_from_state,
    initial_state,
)
from .state_enumerator import all_reachable_states


# ---------------------------------------------------------------------------
# Build a graph from a (State, vstart_active: bool) tuple.
# ---------------------------------------------------------------------------
def pddl_state_to_data(
    state: State,
    objects: Sequence[str] = DOMAIN_OBJECTS,
    *,
    vstart_active: bool = False,
) -> Data:
    """Encode a PDDL state into a torch_geometric.data.Data graph.

    Node features (per object, in `objects` order):
        [on_table, clear, holding] — three 0/1 floats.

    Edge features:
        1 if on(x, y) is in the state.

    Global scalar:
        arm_empty ∈ {0,1}.
    """

    obj_idx = {o: i for i, o in enumerate(objects)}
    n = len(objects)

    node_feats = torch.zeros((n, 3), dtype=torch.float32)
    edges: List[Tuple[int, int]] = []
    for pred in state:
        if pred[0] == "on_table":
            i = obj_idx[pred[1]]
            node_feats[i, 0] = 1.0
        elif pred[0] == "clear":
            i = obj_idx[pred[1]]
            node_feats[i, 1] = 1.0
        elif pred[0] == "holding":
            i = obj_idx[pred[1]]
            node_feats[i, 2] = 1.0
        elif pred[0] == "on" and len(pred) == 3:
            x, y = pred[1], pred[2]
            edges.append((obj_idx[x], obj_idx[y]))

    if edges:
        ei = torch.tensor(edges, dtype=torch.long).t().contiguous()  # (2, E)
    else:
        ei = torch.empty((2, 0), dtype=torch.long)

    arm_empty = 1.0 if ("arm_empty",) in state else 0.0
    global_feat = torch.tensor([arm_empty], dtype=torch.float32)

    data = Data(x=node_feats, edge_index=ei)
    data.global_feat = global_feat
    data.vstart = torch.tensor([1.0 if vstart_active else 0.0], dtype=torch.float32)
    return data


# ---------------------------------------------------------------------------
# Build the supervised dataset by enumerating reachable states.
# ---------------------------------------------------------------------------
def build_supervised_dataset(
    *,
    objects: Sequence[str] = DOMAIN_OBJECTS,
) -> List[Tuple[Data, np.ndarray]]:
    """Return list of (Data, target_feature_vec) pairs.

    For each reachable state we emit two supervision samples: one with vstart
    active (only valid for the initial state) and one without. In practice,
    vstart=True only happens for the very first sample, but we keep the data
    interface uniform.
    """

    pairs: List[Tuple[Data, np.ndarray]] = []
    for state in all_reachable_states():
        for vs in (False,):
            data = pddl_state_to_data(state, objects, vstart_active=vs)
            tgt = features_from_state(state, vstart_active=vs)
            pairs.append((data, tgt))

    # Add the initial state with vstart=True.
    init_data = pddl_state_to_data(initial_state(), objects, vstart_active=True)
    init_tgt = features_from_state(initial_state(), vstart_active=True)
    pairs.insert(0, (init_data, init_tgt))
    return pairs


# ---------------------------------------------------------------------------
# The relational encoder
# ---------------------------------------------------------------------------
class RelationalFeatureEncoder(nn.Module):
    """GIN-style GNN producing a 4-dim Boolean feature vector.

    训练期间接受监督学习: 输入 Data, 输出 4 维 logits, 通过 sigmoid 阈值为 0/1,
    与目标 4 维谓词向量对齐。

    推理 API:
        encoder.encode_state(state, vstart_active) -> np.ndarray[4]
    """

    def __init__(
        self,
        in_dim: int = 3,
        hidden_dim: int = 16,
        out_dim: int = 4,
        n_layers: int = 3,
    ) -> None:
        super().__init__()
        self.in_dim = in_dim
        self.hidden_dim = hidden_dim
        self.out_dim = out_dim

        # An MLP used inside each GINConv layer.
        def _mlp(d_in: int, d_out: int) -> nn.Sequential:
            return nn.Sequential(
                nn.Linear(d_in, d_out),
                nn.ReLU(),
                nn.Linear(d_out, d_out),
                nn.ReLU(),
            )

        self.gins = nn.ModuleList()
        for i in range(n_layers):
            d_in = in_dim if i == 0 else hidden_dim
            self.gins.append(GINConv(_mlp(d_in, hidden_dim), train_eps=True))

        # global feature: arm_empty & vstart are concat'd to the readout
        # (两个全局标量)
        self.global_proj = nn.Linear(hidden_dim + 2, hidden_dim)
        self.head = nn.Linear(hidden_dim, out_dim)

    def forward(self, data: Data) -> torch.Tensor:
        x, ei = data.x, data.edge_index
        # Build batch index for global pooling if not present.
        batch = getattr(data, "batch", None)
        if batch is None:
            batch = torch.zeros(x.size(0), dtype=torch.long, device=x.device)

        for gin in self.gins:
            x = gin(x, ei)
            x = F.relu(x)

        g = global_add_pool(x, batch)            # (B, hidden_dim)
        gf = data.global_feat.view(-1, 1)
        vs = data.vstart.view(-1, 1)
        # If batched into a single graph, both are (1,1); repeat to (B,1).
        if gf.size(0) == 1 and g.size(0) > 1:
            gf = gf.expand(g.size(0), -1)
            vs = vs.expand(g.size(0), -1)
        g = torch.cat([g, gf, vs], dim=-1)
        g = self.global_proj(g)
        g = F.relu(g)
        logits = self.head(g)   # (B, 4)
        return logits

    # ------------------------------------------------------------------ utils
    @torch.no_grad()
    def encode_state(
        self,
        state: State,
        *,
        vstart_active: bool = False,
        objects: Sequence[str] = DOMAIN_OBJECTS,
        threshold: float = 0.5,
    ) -> np.ndarray:
        """Inference: returns 0/1 numpy vector of length 4."""

        self.eval()
        data = pddl_state_to_data(state, objects, vstart_active=vstart_active)
        logits = self.forward(data)
        probs = torch.sigmoid(logits)
        bits = (probs >= threshold).float()
        return bits.squeeze(0).cpu().numpy()


# ---------------------------------------------------------------------------
# Training loop (tiny; the dataset is a few samples)
# ---------------------------------------------------------------------------
def train_relational_encoder(
    *,
    epochs: int = 1000,
    lr: float = 5e-2,
    hidden_dim: int = 16,
    n_layers: int = 3,
    seed: int = 0,
    verbose: bool = False,
) -> Tuple[RelationalFeatureEncoder, List[float]]:
    """Train the encoder with supervised targets; returns (model, loss_history)."""

    torch.manual_seed(seed)
    np.random.seed(seed)

    dataset = build_supervised_dataset()
    if not dataset:
        raise RuntimeError("Empty supervised dataset — check the enumerator.")

    # Wrap into a Batch once per sample (each graph is its own batch).
    losses: List[float] = []
    model = RelationalFeatureEncoder(hidden_dim=hidden_dim, n_layers=n_layers)
    optim = torch.optim.Adam(model.parameters(), lr=lr)

    for ep in range(epochs):
        ep_loss = 0.0
        np.random.shuffle(dataset)
        for data, tgt in dataset:
            optim.zero_grad()
            logits = model(data)                          # (1, 4)
            target = torch.tensor(tgt, dtype=torch.float32).unsqueeze(0)
            loss = F.binary_cross_entropy_with_logits(logits, target)
            loss.backward()
            optim.step()
            ep_loss += loss.item()
        ep_loss /= len(dataset)
        losses.append(ep_loss)
        if verbose and (ep == 0 or (ep + 1) % 200 == 0 or ep == epochs - 1):
            print(f"  encoder epoch {ep+1:4d} | loss={ep_loss:.4f}")

    return model, losses


__all__ = [
    "RelationalFeatureEncoder",
    "build_supervised_dataset",
    "pddl_state_to_data",
    "train_relational_encoder",
]
