## CFG 与 TransitionSystem 的模型检测关联

### 语义网络、Petri网与迁移系统的扩展应用

### Curry-Howard Correspondence：从自动机到文法（符号自动机）

### 域控制知识（DCK）编译为PDDL

域控制知识（Domain Control Knowledge, DCK）通过缩减搜索空间，能够有效地提升规划生成的效率。在各类DCK表现形式中，程序性DCK（Procedural DCK）因其对规划框架的自然规范支持而备受瞩目。然而，遗憾的是，当前大多数主流规划器并未配备利用程序性DCK所必需的机制。为填补这一缺陷，本研究提出将程序性DCK直接编译为PDDL2.1格式，从而使任何兼容PDDL2.1的规划器均能够利用其优势。

本文的贡献主要体现在三个方面。首先，针对类似Algol风格的过程语言，提出了一种基于PDDL的语义框架，该语言可用于在规划问题中精确指定DCK。其次，提供了多项式时间算法，可将ADL规划实例与DCK程序联合转换为等价的无程序PDDL2.1实例，其规划结果恰好是那些严格遵循原程序约束的规划方案。第三，论证了所生成的规划实例极为适合由独立于领域的启发式规划器进行求解。为此，提出了三种方法为翻译后的实例计算领域无关的启发式函数，并在必要时利用翻译过程的固有属性来引导搜索。在面向经典PDDL规划基准的实验评估中，研究结果表明，程序性DCK的编译方法能够显著提升启发式搜索规划器的性能表现。本研究的翻译器已实现并可在线获取。

相关研究文献可参考：[ICAPS 2007 相关论文](https://aaai.org/Library/ICAPS/2007/icaps07-004.php) 以及 [arXiv 预印本](https://arxiv.org/abs/1910.04999)。

### 广义规划与过程域控制知识

广义计划（Generalized Planning）旨在生成对一组规划问题均有效的单一解决方案。本文论证了如何利用过程域控制知识（Procedural Domain Control Knowledge, DCK）来表达并计算广义计划。我们提出了一种"分而治之"（Divide and Conquer）的方法论框架，首先针对代表若干子任务的一组规划问题生成过程性DCK，随后将其编译为面向整体广义计划问题的可调用过程。本文所提出的过程调用机制支持任意形式的嵌套与递归过程调用，并在PDDL语言层面实现，从而确保现成的规划器能够计算并利用过程性DCK。实验结果表明，将程序化DCK作为可调用过程引入现成的经典规划器，能够在涵盖非平凡领域的广泛问题域中有效计算广义计划。

相关研究可参考：[Segovia 等人的广义规划与过程DCK研究](https://bibbase.org/network/publication/segovia-jimenez-jonsson-generalizedplanningwithproceduraldomaincontrolknowledge)。

### 用于生成代码决策图

相关研究主页：[Javier Segovia-Aguas 个人主页](https://jsego.github.io/)

### 游戏智能体规划与寻址等应用

**StarPlanner** 关于 GOAP（Goal-Oriented Action Planning）的设计与翻译，可参考知乎专栏文章：[游戏AI规划：StarPlanner与GOAP](https://zhuanlan.zhihu.com/p/578323828)。
