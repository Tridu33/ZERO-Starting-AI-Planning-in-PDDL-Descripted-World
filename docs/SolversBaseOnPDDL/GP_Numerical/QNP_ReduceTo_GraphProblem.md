[QN_GraphPlanner本地文件](file:///D:/tridu33/Py/jupyternotebook/QN_GraphPlanner)

Qualitative Number Problem 输入文本文件格式：$Q = \langle F, V, I, O, G \rangle$

其中：

> 状态编码 $S = \langle F, V \rangle$ 为一个二进制转十进制之数值。例如，状态 $S_{16} = \{f_1, \neg f_2, \neg f_3, v_1 > 0, v_2 > 0\}$ 编码为二进制 $10000$，即十进制 $16$。经此操作，每个独立状态 $S = \langle F, V \rangle$ 均被唯一地编码为一个数值。

- $F$：Boolean proposition

  | $f_1$ | ...  | $f_n$ | $\neg f_1$ | ...  | $\neg f_n$ |
  | ----- | ---- | ----- | --------- | ---- | --------- |
  | 1     | 1    | 1     | 0         | 0    | 0         |

- $V$：

  | $v_1 > 0$ | ...  | $v_m > 0$ | $v_1 = 0$ | ...  | $v_m = 0$ |
  | --------- | ---- | --------- | --------- | ---- | --------- |
  | 0         | 0    | 0         | 1         | 1    | 1         |

- $I$ 为起始状态

- $G$ 为目标状态，同样仅为一个状态编码。

- $O$ 为动作集 $\{a_1, a_2, a_3, a_4, \ldots\}$，定义为状态间的映射关系，并允许通过缺省值自动枚举状态。例如，"放下石头"动作的唯一直观形式化表示为 $\langle \neg E, E \rangle$，即描述动作所对应的状态变迁。

注：在 QNP 问题中，原始问题通常使用 $V = \{v_1, v_2, v_3, \ldots\}$ 作为非确定性动作 $a_x$ 的 if-condition 条件判断依据，用以决定当前状态采取动作 $a_x$ 后的后继影响 effects。以积木世界为例，确定性动作 Pick-above-x（捡起 $x$ 上方积木）：若条件 if $(x \text{上方积木数量} n - 1 \neq 0)$ 成立，则执行动作 Pick-above-x 的后继状态为 $\neg \text{clear}(x)$（非空）；若条件 if $(x \text{上方积木数量} n - 1 \neq 0)$ 不成立，则执行动作 Pick-above-x 的后继状态为 $\text{clear}(x)$（空）。

在本算法求解问题时，首先考虑松弛问题（relaxed problem），即放松动作执行后 if-condition 条件判断决定后续结果 effect 的约束，暂时假设动作 Pick-above-x 是非确定性的，执行后既可能产生 $\text{clear}(x)$，也可能产生 $\neg \text{clear}(x)$。待应用图论算法找到一条从 $S_i$ 到 $S_G$ 的有向有环通路图 $G_{\text{Solution}}$ 之后，再恢复 if-condition 的功能，从而生成唯一可执行的动作序列 $\{a_1, a_1, a_1, a_2, a_3, \ldots\}$ 作为解。

---

首先将标准 QNP 问题归约为经典有向图问题 $G = \langle \text{Node节点}, \text{Edges边} \rangle$：

QNP 中的 $S = \langle F, V \rangle$（包含有限状态集）归约为图 $G$ 中的节点集 Nodes；

QNP 中的动作集 $O$ 则归约为图 $G$ 中节点之间的有向边 Edges。

原问题 QNP 由此转化为在一张有向有环图 $G$ 中寻找一条从 $S_i$ 到 $S_G$ 的有向有环通路图 $G_{\text{Solution}}$ 的问题。

- **算法第一步**：利用《系统工程》中的解析结构模型化技术（ISM 算法），去除孤立节点（通过缺省值自动枚举但"不可能发生"的状态）以及不包含 $S_i, S_G$ 的**有向有环子图** $G_{\text{pruning}}$。至于为何不从 $S_i$ 开始枚举动作集 $O$ 破圈搜索至 $S_G$？理论上亦可，结果应一致。总之，建立图 $G = \langle N, E \rangle$ 后，以矩阵格式表达并用 ISM 算法处理更为便捷。
- **算法第二步**：破环。采用 Tarjan 等图论算法识别强连通分量（SCC），（可逆地）合并 SCC 为若干"虚拟节点"，原图经合并后转变为一张**有向无环图** $G_{\text{DirectedAcyclicGraph}}$。
- **算法第三步**：针对有向无环图 $G_{\text{DirectedAcyclicGraph}}$，寻找从起始节点到目标节点的路径。可实现该功能的算法众多，可直接采用 Dijkstra 算法找到一条从 $S_i$ 到 $S_G$ 的**有向有环通路图** $G_{\text{HalfSolution}}$。
- **算法第四步**：对通路图 $G_{\text{HalfSolution}}$ 应用第二步的可逆合并操作，解除 SCC 的合并（第二步需记录入度节点和出度节点，以便 SCC 还原时使用），从而得到**有向有环通路图** $G_{\text{Solution}}$。
- 随后，从松弛约束（relaxed problem）收紧为前文所述的"含 if-condition 的确定性动作"，应用数值变量 $V$ 的 if-condition 条件判断功能，从图 $G_{\text{Solution}}$ 生成唯一可执行的策略（Policy）：$S_{F,V} \rightarrow O_{\text{actions}}$，从而得到对应的动作序列 $\{a_1, a_1, a_1, a_2, a_3, \ldots\}$ 解。

![qnp图法设计_1598498581_30912](_v_images\qnp图法设计_1598498581_30912.png)
