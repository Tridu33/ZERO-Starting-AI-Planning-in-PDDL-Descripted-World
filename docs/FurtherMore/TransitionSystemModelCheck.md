# 迁移系统模型检测与 QNP

本研究致力于寻找一种能够描述并验证包含分支（branch）和循环（while loop）等控制结构的程序/控制器控制流图（Control Flow Graph）的逻辑体系。首先考察IC3模型检测（IC3 Model Checking）的相关理论与方法。

## IC3 模型检测的核心文献

1. **SAT-Based Model Checking without Unrolling**
2. **IC3 - Flipping the E in ICE**
3. **Understanding IC3**
4. **Efficient Implementation of Property Directed Reachability**

上述文献构成了IC3算法（亦称属性导向可达性分析，Property Directed Reachability, PDR）的理论基础，为验证包含循环与分支结构的迁移系统提供了高效的形式化方法。

## 学习资源

可参考知乎专栏文章：[软工方法论之形式化方法NuSMV学习笔记](https://zhuanlan.zhihu.com/p/343685908)，该文详细介绍了NuSMV模型检测工具的使用方法与形式化验证的基本概念。

## 与 QNP 的联系

QNP（定性数值规划问题）所定义的抽象结构可视为一种迁移系统。将IC3等模型检测技术应用于QNP框架，有助于实现对包含循环与分支结构的广义规划方案的形式化验证与终止性分析，从而架设规划生成与程序验证之间的桥梁。
