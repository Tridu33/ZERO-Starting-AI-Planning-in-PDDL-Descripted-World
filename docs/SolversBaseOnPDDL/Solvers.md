#  solver汇总

MyND

PRP

FOND-SAT

PRP_planner-for-relevant-policies

一般两条路：

Top-Down(与或树{或者也可以理解为ControlFlowGraph}在图中搜索-->algorithm-like 的policy，在我看来，这就是符号化goto语句的底层汇编算法等价描述) 



&& 



Bottom-Up(生成实例经典规划中完善补全抽象图，不断响应式打补丁)，FONS-SAT可以看作文法自动机，用符号SAT可满足性求解，就我的理解来说，其实属于Top-Down“求解”。

如：Merging Example Plans into Generalized Plans forNon-deterministic Environments和Directed Search for Generalized Plans Using Classical Planners

> 正如Dijkstra在他书中说到意思，编程是严谨思考推理得到的算法。
>
> 图灵开启的自动编程故事，相信plan会是一个美丽的解法。

QNP其实就是在模拟有while循环的Linked list reverse受到的启发，才提出来的，这类问题的解子图policy其实就是**包含while循环的algorithm**。