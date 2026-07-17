# GOLOG and PDDL
What is the Relative Expressiveness

https://jens-classen.net/pub/EyerichEtAl2006.pdf

## PDDL+Golog

基于 PDDL 所生成的规划方案之执行，可与常规的 Golog 程序及执行监视机制相结合。

https://www.fawkesrobotics.org/projects/golog-cp/

## Prolog 验证

[Source Code Verification for Embedded Systems using Prolog](
https://arxiv.org/abs/1701.00630)

与安全关键系统相关的嵌入式软件必须具备高度的可靠性，因而需要经过充分的测试验证，航空航天系统尤为如此。验证程序的常用技术之一是对其抽象语法树（Abstract Syntax Tree, AST）进行分析。逻辑编程语言 Prolog 以其优雅的语法结构，尤为适合处理树状数据结构的分析任务。此外，Prolog 还提供了若干进行深度分析的内在优势：一方面，其自身包含多种高效处理树或图数据结构的内建机制；另一方面，Prolog 的不确定性与回溯机制可便捷地测试程序流程的各种可能变体。Prolog 基于规则的方法论允许以简洁明了的方式对验证目标加以形式化表征。

本文介绍了借助 Prolog 对 Flash 文件系统源代码进行验证的方法。Flash 文件系统采用 C++ 编写，专为卫星应用场景而设计开发。本研究将给定的 C++ 源代码抽象语法树转换为 Prolog 事实（facts），进而推导出调用图（call graph）与执行序列树（execution tree），并针对预定义的验证目标对其进行系统性测试。由控制结构所导引的不同程序流分支，通过回溯机制生成为完整的执行序列子树。最终，这些子树在 Prolog 环境中得到验证。

本文通过一个案例研究对所提方法加以具体说明：我们使用实时操作系统 RODOS，在嵌入式软件中搜索信号量（semaphore）的不正确应用模式。本研究依托计算树逻辑（Computation Tree Logic, CTL），并在 Prolog 中设计了一种嵌入式的领域特定语言（Domain-Specific Language, DSL）以表达验证目标。
