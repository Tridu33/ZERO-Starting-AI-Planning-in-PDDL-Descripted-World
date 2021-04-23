

 Fluent


https://en.wikipedia.org/wiki/Fluent_(artificial_intelligence)


fluent 

  STRIPS语言

您可以使用在线应用程序[Strips-Fiddle](https://stripsfiddle.herokuapp.com/)尝试不同的STRIPS PDDL域和问题。尝试任何示例领域，或创建一个帐户来设计自己的人工智能计划领域和问题。

要将基于STRIPS的AI规划集成到您的应用程序或游戏中，可以使用node.js [strips](https://www.npmjs.com/package/strips)库，该库支持广度优先，深度优先和A *搜索。Strips库的[github主页](https://github.com/primaryobjects/strips/)提供了对该库的更高层次的概述，其中包括[Starcraft](https://github.com/primaryobjects/strips/#starcraft)域的示例。


https://en.wikipedia.org/wiki/Stanford_Research_Institute_Problem_Solver 入门看这里 http://www.primaryobjects.com/2015/11/06/artificial-intelligence-planning-with-strips-a-gentle-introduction/

[机械之心提到过一下这个](https://www.jiqizhixin.com/graph/technologies/9ad9b15f-b57d-4a18-b4fa-6d1728c35b63)简介

STRIPS 表达式一种以行动为中心的表示，它对于每个动作（action）来说，都需要指定这个动作所获得的效果（effect）。一个这样的表示就是**STRIPS representation**。“斯坦福研究院问题解决器”(Stanford Research Institute Problem Solver)的缩写，

首先，将描述世界的特征划分为原始的**primitive**和派生的**primitive**特征。一定数量的子句用来确定从任何给定状态的原始**primitive**特征值得出的派生derived特征的值。STRIPS表示基于先前状态和之前agent所采取的操作，来确定一个状态下的原始特征值，

**STRIPS representation**是基于大多数事物不受单个动作影响的观点设计的。对于每一个动作，当动作可行时，STRIPS models中原始**primitive**特征值会被动作所影响。动作的效果依赖于**STRIPS assumption**: 动作描述中所提到的所有原始特征保持不变。

一个动作的**STRIPS representation**包括：

-   前置条件**precondition**，它是一组值的赋值，操作发生时，它们必须是True的。
-   效果**effect**，它是一组结果赋值给那些由于动作而改变的原始特征。

原始特征V在动作*act*行为后具有v值，如果V= v在行为列表中，或者在act的效果列表中没有提到V，则V在动作*act*前立即具有v值。非原始的特性可以从原始特性的值中派生出来。

当变量是布尔值时，有时将效果划分为一个删除列表delete list是很有用的，其中包括那些可能导致false的变量，以及一个add list添加列表，其中包含导致True的变量。

例:Rob拿起咖啡(puc)的动作如下，STRIPS representation:

```
precondition
[cs,$\neg rhc$
 effect 
[rhc]
```

|年份 |   事件  |  相关论文/Reference |
|----|-----|---|
|1971  |  Fikes, R. E., & Nilsson, N. J.提出STRIPS         |   Fikes, R. E., & Nilsson, N. J. (1971). STRIPS: A new approach to the application of theorem proving to problem solving. Artificial intelligence, 2(3-4), 189-208.|
|1992  |  H. A. Kautz and B. Selman提出的Satplan           |    Kautz, H. A., & Selman, B. (1992, August). Planning as Satisfiability. In ECAI (Vol. 92, pp. 359-363).|
|1993  |  Fikes, R. E., & Nilsson, N. J.对STRIPS进行回顾    |   Fikes, R. E., & Nilsson, N. J. (1993). STRIPS, a retrospective. Artificial Intelligence, 59(1-2), 227-232.|
|1997  |  Blum, A. L., & Furst, M. L.提出一种快速的图规划算法 |    Blum, A. L., & Furst, M. L. (1997). Fast planning through planning graph analysis. Artificial intelligence, 90(1-2), 281-300.|
|2010  |  Galuszka, A., & Swierniak, A.在多机器人中基于STRIPS和非合作博弈的规划算法 |  Galuszka, A., & Swierniak, A. (2010). Planning in multi-agent environment using strips representation and non-cooperative equilibrium strategy. Journal of Intelligent and Robotic Systems, 58(3-4), 239-251.|












# JS-STRIP





https://github.com/primaryobjects/strips

AI Automated Planning with STRIPS and PDDL in Node.js

https://www.npmjs.com/package/strips

```
npm install strips
```

