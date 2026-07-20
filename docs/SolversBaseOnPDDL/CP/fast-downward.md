# Fast Downward 规划器

[Fast Downward 优于 FF 的相关讨论](https://stackoverflow.com/questions/18945035/fast-forward-and-pddl-is-the-computed-solution-the-best)

[Fast Downward 官方网站](http://www.fast-downward.org/)

[GitHub 仓库](https://github.com/aibasel/downward)

[Haskell 包（含 gripper 示例）](https://hackage.haskell.org/package/fast-downward)

[Planning Wiki 参考文档](https://planning.wiki/ref/planners/fd)

Jendrik Seipp 7:54 PM
Shameless plug: I'll be giving an ICAPS tutorial about "Evaluating Planners with Downward Lab" on October 20 at 19:00 UTC. We'll talk about best practices for Downward Lab experiments and there'll be a Q&A session, so bring your questions!

[ICAPS 2020 Downward Lab 教程](https://icaps20subpages.icaps-conference.org/tutorials/evaluating-planners-with-downward-lab/)

## Lab 与 Downward Lab

[Lab GitHub 仓库](https://github.com/aibasel/lab)

Lab 是一个基于 Python 的软件包，专门用于在基准测试集上评估求解器的性能。实验既可在单台计算机上执行，亦可在计算机集群上运行。该软件包还集成了用于解析实验结果和生成分析报告的相关代码。

Downward Lab 这一 Python 软件包为 Fast Downward 规划系统的实验运行提供了便捷支持。它基于通用的实验软件包 Lab 构建。目前，Lab 与 Downward Lab 采取统一发布的方式。

- 代码：[Lab GitHub 仓库](https://github.com/aibasel/lab)
- 文档：[Lab 文档](https://lab.readthedocs.io)
- 引用方式：请参照 Downward Lab 的引用说明。
