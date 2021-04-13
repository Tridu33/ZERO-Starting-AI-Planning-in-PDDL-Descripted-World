# grahPlan

http://www.ai.mit.edu/courses/16.412J/Graphplan.html 

Graphplan是一种基于计划图概念的计划算法。计划图表示基于当前级别的可行算子的应用在将来级别中可以实现的事实。第一级代表初始状态，最后一级包含出现在目标状态中的所有事实（以及可能的许多其他事实）。事实和操作员之间的互斥关系在计划图的每个级别上都得到维护。生成计划图后，Graphplan从目标（最后）级别向后搜索以生成可行的计划。

此处提供了源代码以及有关构建和运行可执行文件的说明。源代码在C中，并提供了一个Makefile。构建和运行可执行文件应该在任何使用C的Unix系统上都可以使用。示例问题（事实和操作员文件）也包括在内。

可以在[Graphplan主页](http://www-2.cs.cmu.edu/~avrim/graphplan.html)上找到有关Graphplan的更多详细信息 。出色的参考论文是：
[A. Blum，M. Furst，“通过规划图分析进行快速规划”](http://www.ai.mit.edu/courses/16.412J/graphplan.ps)，《*人工智能*[》 ](http://www.ai.mit.edu/courses/16.412J/graphplan.ps)，90：281--300（1997）。这是描述算法及其实现的原始论文。




(PDF) NGP: Numerical Graph Planning.

https://fai.cs.uni-saarland.de/hoffmann/metric-ff.html#:~:text=Extending%20FF%20to%20Numerical%20State%20Variables%2C%20in%3A%20Proceedings,as%20used%20in%20the%203rd%20International%20Planning%20Competition.

















