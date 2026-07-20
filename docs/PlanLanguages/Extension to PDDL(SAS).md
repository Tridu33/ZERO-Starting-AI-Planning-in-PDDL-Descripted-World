# PDDL 扩展：层次化规划与 SAS 形式化

## 层次化规划扩展

PDDL 语言自诞生以来经历了多方向的扩展，其中层次化规划（Hierarchical Planning）是一个重要的研究方向。相关研究提案包括：

- **基于 PDDL 的层次化规划扩展**（An Extension to PDDL for Hierarchical Planning）—— 旨在将层次化任务网络（HTN）规划的概念引入 PDDL 框架。
- **面向非确定性、有限感知与迭代条件规划的 PDDL 扩展**（Extending PDDL to Nondeterminism, Limited Sensing and Iterative Conditional Plans）—— 扩展 PDDL 以支持不确定环境下的规划。
- **层次化规划与拓扑抽象的 PDDL 扩展**（Extending PDDL for Hierarchical Planning and Topological Abstraction）—— 结合拓扑抽象方法增强层次化规划能力。

上述提案曾在 ICAPS 2003 的 PDDL 专题研讨会上进行讨论，相关文献参见：[ICAPS 2003 PDDL 研讨会论文集](https://users.cecs.anu.edu.au/~thiebaux/workshops/ICAPS03/proceedings/PDDL-ICAPS03.pdf)。

## SAS（Simple Additive Structure）形式化扩展

SAS（简单加性结构，Simple Additive Structure）是 PDDL 形式化扩展的重要方向之一。SAS 形式化方法将规划问题表示为多值变量的集合，每个变量具有有限的取值域，从而在表达能力上优于经典的二值 STRIPS 表示。SAS 表示特别适用于需要描述对象属性状态间复杂依赖关系的规划任务，并在许多现代规划求解器中得到了广泛应用。

## PDDL 扩展全景

[维基百科上列举了 PDDL 的各类扩展](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language)，涵盖层次化规划、时序规划、数值规划、不确定性规划等多个方向，构成了一个丰富的扩展生态系统。
