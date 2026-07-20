# STRIPS 语言

## Fluent（流利性）

[Fluent（人工智能中的流利性概念）](https://en.wikipedia.org/wiki/Fluent_(artificial_intelligence))

您可借助在线应用程序 [Strips-Fiddle](https://stripsfiddle.herokuapp.com/) 探索并实验多种 STRIPS PDDL 领域及问题实例。您既可直接运行内置的示例领域，亦可注册账户以自行设计人工智能规划领域与相应问题。

若需将基于 STRIPS 的 AI 规划功能集成至您的应用程序或游戏之中，可使用 Node.js [strips](https://www.npmjs.com/package/strips) 库。该库支持广度优先搜索、深度优先搜索以及 A\* 搜索等经典图搜索算法。[Strips 库的 GitHub 主页](https://github.com/primaryobjects/strips/) 对该库进行了更高层次的系统性概述，并包含[星际争霸（StarCraft）](https://github.com/primaryobjects/strips/#starcraft)领域的示例。

[斯坦福研究院问题解决器（STRIPS）](https://en.wikipedia.org/wiki/Stanford_Research_Institute_Problem_Solver)关于入门指导，可参阅：[人工智能规划与 STRIPS 入门指南](http://www.primaryobjects.com/2015/11/06/artificial-intelligence-planning-with-strips-a-gentle-introduction/)

[机器之心曾对此进行过简要介绍](https://www.jiqizhixin.com/graph/technologies/9ad9b15f-b57d-4a18-b4fa-6d1728c35b63)

## STRIPS 表示范式

STRIPS 表达式是一种以行动为中心的表示范式，其对每个动作（action）均要求明确指定该动作所引发的效果（effect）。此类表示范式被称为 **STRIPS 表示（STRIPS representation）**。STRIPS 系"斯坦福研究院问题解决器"（Stanford Research Institute Problem Solver）之缩写。

首先，可将描述世界状态的特征划分为原始特征（**primitive**）与派生特征（**derived**）两大类别。通过若干子句规则，可从任意给定状态下原始特征的值推导出派生特征的值。STRIPS 表示法依据先前状态以及智能体（agent）此前所执行的操作，来确定当前状态下原始特征的具体取值。

**STRIPS 表示**的设计哲学基于如下基本观察：绝大多数事物并不因单个动作而发生改变。对于每个动作而言，当该动作可行时，STRIPS 模型中的原始特征值将受到该动作的影响。动作的效果依赖于 **STRIPS 假设（STRIPS assumption）**：凡动作描述中未曾提及的原始特征均维持原值不变。

一个动作的 **STRIPS 表示**包含以下组成部分：

- **前置条件（precondition）**：一组赋值约束，操作执行时这些条件必须为真（True）。
- **效果（effect）**：一组结果赋值，用以刻画那些因动作执行而发生改变的原始特征。

原始特征 V 在动作 *act* 执行后取值为 v，当且仅当 V=v 出现在该动作的效果列表之中；若效果列表中未提及 V，则 V 在动作 *act* 执行前即已具有该值。非原始（即派生）特征的值可从原始特征的值经由推导规则得出。

当所涉及的变量为布尔类型时，将效果划分为**删除列表（delete list）**与**添加列表（add list）**尤为实用：删除列表包含那些在执行后取值为假（False）的变量，而添加列表则包含那些在执行后取值为真（True）的变量。

示例：机器人 Rob 拿起咖啡（pick up coffee, puc）动作的 STRIPS 表示如下：

```
precondition
[cs,¬rhc]
effect
[rhc]
```

## STRIPS 发展历程

| 年份 | 事件                                                         | 相关论文/Reference                                            |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1971 | Fikes, R. E., & Nilsson, N. J. 提出 STRIPS 形式化框架        | Fikes, R. E., & Nilsson, N. J. (1971). STRIPS: A new approach to the application of theorem proving to problem solving. Artificial intelligence, 2(3-4), 189-208. |
| 1992 | H. A. Kautz and B. Selman 提出 Satplan 方法                  | Kautz, H. A., & Selman, B. (1992, August). Planning as Satisfiability. In ECAI (Vol. 92, pp. 359-363). |
| 1993 | Fikes, R. E., & Nilsson, N. J. 对 STRIPS 进行回顾性分析       | Fikes, R. E., & Nilsson, N. J. (1993). STRIPS, a retrospective. Artificial Intelligence, 59(1-2), 227-232. |
| 1997 | Blum, A. L., & Furst, M. L. 提出一种快速的图规划算法         | Blum, A. L., & Furst, M. L. (1997). Fast planning through planning graph analysis. Artificial intelligence, 90(1-2), 281-300. |
| 2010 | Galuszka, A., & Swierniak, A. 提出基于 STRIPS 与非合作博弈的多智能体规划方法 | Galuszka, A., & Swierniak, A. (2010). Planning in multi-agent environment using strips representation and non-cooperative equilibrium strategy. Journal of Intelligent and Robotic Systems, 58(3-4), 239-251. |

## JS-STRIPS 实现

[GitHub: primaryobjects/strips](https://github.com/primaryobjects/strips)

AI Automated Planning with STRIPS and PDDL in Node.js

[npm: strips 包](https://www.npmjs.com/package/strips)

```
npm install strips
```
