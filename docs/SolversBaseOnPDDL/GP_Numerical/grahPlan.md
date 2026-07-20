# GraphPlan：基于规划图的经典规划算法

[GraphPlan 课程资料](http://www.ai.mit.edu/courses/16.412J/Graphplan.html)

Graphplan 是一种基于规划图（planning graph）概念的规划算法。规划图刻画了在当前层级可行操作符作用下，于后续层级中可实现的事实集合。第一级表示初始状态，最后一级则包含目标状态中出现的全部事实（以及可能附带的其他诸多事实）。事实与操作符之间的互斥关系在规划图的每个层级上均加以维护。生成规划图后，Graphplan 从目标层级（即最后一级）开始反向搜索，以生成可行的规划方案。

上述链接提供了源代码及相关说明，涵盖构建与运行可执行文件的详细指引。源代码采用 C 语言编写，并附有 Makefile。在任何支持 C 语言的 Unix 系统上均可完成构建与运行。示例问题（包含事实文件与操作符文件）亦一并提供。

有关 Graphplan 的更多详细信息，可参阅 [GraphPlan 主页](http://www-2.cs.cmu.edu/~avrim/graphplan.html)。权威参考文献如下：

- [A. Blum, M. Furst, "Fast Planning Through Planning Graph Analysis"](http://www.ai.mit.edu/courses/16.412J/graphplan.ps), *Artificial Intelligence*, 90: 281–300 (1997). 该文为描述算法及其实现的原始论文。

数值图规划（Numerical Graph Planning, NGP）相关文献：

[Extending FF to Numerical State Variables](https://fai.cs.uni-saarland.de/hoffmann/metric-ff.html#:~:text=Extending%20FF%20to%20Numerical%20State%20Variables%2C%20in%3A%20Proceedings,as%20used%20in%20the%203rd%20International%20Planning%20Competition)
