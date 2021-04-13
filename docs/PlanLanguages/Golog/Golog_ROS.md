

# GOLOG and PDDL  What is the RelativeExpressiveness

https://jens-classen.net/pub/EyerichEtAl2006.pdf



# PDDL+Golog

基于PDDL的生成的计划的执行与常规的Golog程序和执行监视相结合。

https://www.fawkesrobotics.org/projects/golog-cp/

# prolog验证

[Source Code Verification for Embedded Systems using Prolog](
https://arxiv.org/abs/1701.00630)

与系统相关的嵌入式软件需要可靠，因此必须经过良好的测试，尤其是对于航空航天系统而言。验证程序的常用技术是对其抽象语法树（AST）的分析。可以使用逻辑编程语言Prolog优雅地分析树结构。此外，Prolog还提供了进行全面分析的更多优势：一方面，它本身提供了多种选项来有效地处理树或图形数据结构。另一方面，Prolog的不确定性和回溯功能可轻松测试程序流程的各种变化。Prolog基于规则的方法允许以简洁明了的方式表征验证目标。
在本文中，我们介绍了在Prolog的帮助下验证Flash文件系统源代码的方法。Flash文件系统是用C ++编写的，并且是专门为在卫星中使用而开发的。我们将给定的C ++源代码抽象语法树转换为Prolog事实，并得出调用图和执行序列（树），然后针对验证目标对它们进行进一步测试。由控制结构引起的不同程序流分支是通过回溯作为完整执行序列的子树而得出的。最后，这些子树在Prolog中进行了验证。
我们通过一个案例研究来说明我们的方法，其中我们使用实时操作系统RODOS在嵌入式软件中搜索信号灯的不正确应用。我们依靠计算树逻辑（CTL）并在Prolog中设计了一种嵌入式领域特定语言（DSL）来表达验证目标。