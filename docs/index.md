[TOC]

# ZERO-Starting AI Planning in PDDL-Descripted World

从零开始的PDDL-Descripted世界AI 规划。

## plan-wiki

https://github.com/nergmada/planning-wiki

https://fai.cs.uni-saarland.de/hoffmann/papers/ki11.pdf Everything You Always Wanted to Know AboutPlanning(But Were Afraid to Ask)



人工智能规划很好的课程资料 https://yawgmoth.github.io/PF-3335/  PF 3335  Artificial Intelligence Planning 课程项目：https://yawgmoth.github.io/PF-3335/project/ 在线版本PPT  https://yawgmoth.github.io/PF-3335/slides/

## Resources

**Tutorials**

Getting Started with PDDL https://fareskalaboud.github.io/LearnPDDL/ 源码 https://github.com/fareskalaboud/LearnPDDL

https://github.com/jan-dolejsi/pddl-reference  


https://planning.wiki/extras

https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language#De_facto_official_versions_of_PDDL

 start-process-stop model.

marketplace.visualstudio.com/items?itemName=jan-dolejsi.pddl 教程


PDDL-editor（基于vs-code的简易规划器） - 寻风者风寻的文章 - 知乎
https://zhuanlan.zhihu.com/p/113874556 

https://www.zhihu.com/column/pddl-basicnote PDDL知乎专栏

youtube.com/watch?v=XW0z8Oik6G8

网站

https://planning.wiki/ github有源码 https://github.com/nergmada/planning-wiki

https://github.com/jan-dolejsi/pddl-reference/tree/master/docs  有关PDDL，计划，历史记录，用法和研究的更多详细信息，请参阅指南。


视频教程：

  - [Learn PDDL by Fares K. Alaboud](https://fareskalaboud.github.io/LearnPDDL/)
  - [Introduction to AI Planning. Part I. (video)](https://www.youtube.com/watch?v=EeQcCs9SnhU)
  - [Introduction to AI Planning. Part II. (video)](https://www.youtube.com/watch?v=FS95UjrICy0)

http://planning.domains/


api.planning.domains

solver.planning.domains

开源源码
github.com/jan-dolejsi/vscode-pddl

github.com/jan-dolejsi/vscode-pddl-samples

## VS code PDDL插件

VS code PDDL插件有很多相关研究链接

vscode 插件pddl :AI Planning and PDDL support in VS Code


youtube.com/watch?v=XW0z8Oik6G8&feature=youtu.be

Below you can find a collection of resources for writing, learning and using PDDL and planning. For more information on what these tools and resources are and how they can help, please visit the [additional resources](https://github.com/nergmada/planning-wiki/blob/master/extras) page.

- [Planning.Domains](http://planning.domains/)
- Planner Tools
  - [VAL - The Plan Validator](https://nms.kcl.ac.uk/planning/software/val.html)
  - [ROSPlan - Planning in ROS](https://github.com/KCL-Planning/ROSPlan/)
  - [PlanSys2 - Planning in ROS2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)
  - [Eviscerator - The Planner tester](https://www.github.com/nergmada/eviscerator)
  - [Universal Planning Validator (Under Development)](https://github.com/aig-upf/universal-planning-validator)

https://planning.wiki/extras 介绍 

## solver.planning.domains规划online解决方案


http://solver.planning.domains/

http://planning.domains/


包括：

- api
  http://api.planning.domains/ api查询

https://github.com/AI-Planning/classical-domains PDDL文件的简单集合。当前仅包括经典问题

planning.domains API提供了对广泛的PDDL基准域和问题文件的编程访问。所有物理文件都可以 在GitHub的域存储库中找到。您可以通过克隆存储库或使用下面描述的命令行实用程序来自己获得一份副本。

如果您在PDDL文件中发现任何错误（不完整的集，不良的配方等），请克隆存储库，并将您的修订作为请求请求提交。在合理的情况下，我们还将接受带有全新基准测试集的拉取请求（例如，在新的IPC竞赛之后或作为特定套件的发布）。目前，仅接受经典的PDDL基准（任何PDDL级别/表现力），但是将来我们希望将其扩展到其他更丰富的形式主义（POND，FOND，RDDL等）。

文件集合只是api.planning.domains的第一个组件。该服务的主要方面是提供用于查询，查看和浏览现有域的界面。我们存储并不断更新每个领域和问题的属性。例如，计划成本的上限和下限，域中的要求，问题的经典宽度等。在此页面上，您可以找到api.planning.domains接口的描述以及有关的详细信息用来简化与API交互的工具/库。

该API包含三种类型的对象：

问题：有关每个问题的信息，包括其文件，相应的域文件，问题的统计信息等。
域：每个单独域的信息，包括其描述和该域的各种统计信息。
集合：域集，包括每个IPC的集合，单个计划程序集合等。
免责声明：此刻，API应该被认为处于非常Alpha阶段。希望最终有一种方法可以精确地引用评估软件时使用的基准，但暂时我们仍在修复领域，替换问题集并纠正各种统计数据中的错误。在删除此免责声明之前，我们建议您不要将API用于公务（学术界或其他领域）。

- solver


http://solver.planning.domains/


在线PDDL文件求解器范例教程 ，

可以通过发送指向PDDL文件的链接或直接以JSON格式发送原始PDDL内容来调用软件，以检索或验证计划。

Javascript/pytoon远程调用使用范例 代码


- editor

http://editor.planning.domains/  在线PDDL编辑/求解/验证器


- education

http://education.planning.domains/

学习自动教学计划和建模技术的资源

PPT课间源码和视频教程

## 规划工具们

 [VAL-计划验证器](https://nms.kcl.ac.uk/planning/software/val.html)

[VAL](https://nms.kcl.ac.uk/planning/software/val.html)（也称为验证器）是一种工具，用于根据原始域和问题文件验证计划者生成的解决方案。VAL使您可以在执行操作时遵守计划所需的所有前提条件，同时检查计划是否真正实现了目标。

 [Eviscerator-规划器测试器](https://www.github.com/nergmada/eviscerator)

[Eviscerator](https://www.github.com/nergmada/eviscerator)是为此PDDL参考指南开发的工具，它使我们能够自动测试和识别计划人员支持的PDDL要求。它是一个开放源代码工具，随附用于Linux的持续部署的预构建二进制文件。这意味着您可以下载它并测试计划程序，而不必担心编译。

 [ROSPlan-ROS中的计划](https://github.com/KCL-Planning/ROSPlan/)

[ROSPlan](https://github.com/KCL-Planning/ROSPlan/)是机器人操作系统（ROS）的模块，允许将AI Planning集成到使用ROS的机器人中。ROSPlan允许对机器人环境进行建模，以计划和执行任务。

[Plansys2-在ROS2中进行规划](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)

[Plansys2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)是机器人作业系统，新版本的一个项目**ROS2**，整合规划和机器人。它的目标是成为一个框架，在其中可以轻松集成不同的计划人员以使机器人执行任务。使用[行为树](https://github.com/BehaviorTree/BehaviorTree.CPP)来实现[动作](https://github.com/BehaviorTree/BehaviorTree.CPP)，并且在仓库中有很多[例子](https://github.com/IntelligentRoboticsLabs/ros2_planning_system_examples/)。

 [通用规划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)

[通用计划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)是一种用于验证计划领域和问题的工具。当前，它只能支持经典的计划问题和领域，但是该工具旨在进行扩展以包括时间域和多主体域。如果您需要一个支持比传统计划更多的PDDL高级功能的验证器，请尝试使用VAL（计划验证器）代替。

- PDDL Tools
  - Visual Studio Code
    - [PDDL Plugin for VSCode](https://marketplace.visualstudio.com/items?itemName=jan-dolejsi.pddl)
  - Sublime Text Editor
    - [MyPDDL Plugin for Sublime](https://packagecontrol.io/packages/myPDDL)
  - Atom Text Editor
    - [MyPDDL Plugin for Atom](https://atom.io/packages/mypddl)
  - [Planning.Domains PDDL Editor](http://editor.planning.domains/)
- Learning Resources
  - [Learn PDDL by Fares K. Alaboud](https://fareskalaboud.github.io/LearnPDDL/)
  - [Introduction to AI Planning. Part I. (video)](https://www.youtube.com/watch?v=EeQcCs9SnhU)
  - [Introduction to AI Planning. Part II. (video)](https://www.youtube.com/watch?v=FS95UjrICy0)


http://education.planning.domains/ 

##  Course Materials

Compiled and source course materials (please [contact teacher in this url](mailto:christian.muise@gmail.com) for access to source materials).

 Lecture Slides

| [UniBasel AI Group](https://ai.dmi.unibas.ch/)               | Misc AI and Planning Courses | [Lecture Slides](https://ai.dmi.unibas.ch/forstudents.html) |                                                              |
| ------------------------------------------------------------ | ---------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| [Foundations of Artificial Intelligence (FAI) Group](http://fai.cs.uni-saarland.de/index.html) | Misc AI and Planning Courses | [Lecture Slides](http://fai.cs.uni-saarland.de/teaching/)   | [Planning Source](http://education.planning.domains/lecturer_area/fai-planning.zip) [AI Source](http://education.planning.domains/lecturer_area/fai-ai.zip) |

 Example Assignments

| [Artificial Intelligence (CS) at PUCRS](https://github.com/pucrs-ai-cs) | Felipe Meneguzzi, Mauricio Magnaguagno, Leonardo Rosa Amado | Planning using Heuristic Search assignment focused on implementing the core functions of an automated planner. | [Source Code](https://github.com/pucrs-automated-planning/heuristic-planning) |
| ------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Pacman Capture the Flag in AI Courses](https://ieeexplore.ieee.org/document/8468047) | Nir Lipovetzky, Sebastian Sardina                           | Competition using the Berkley AI Pacman framework. Students use search algoithms, PDDL, classical replanning, minimax, etc. for their agents. | [Competition](https://sites.google.com/view/pacman-capture-hall-fame) [Code](https://bitbucket.org/ssardina-teaching/pacman-contest/src/master/) |
| [ICAPS 2020 Summer School Plan Synthesis](https://icaps20subpages.icaps-conference.org/students/summer-school/icaps-online-summer-school-lab-plan-synthesis/) | Michael Cashmore                                            | This training lab is an introduction to modelling planning problems using the Planning Domain Definition Language (PDDL). | [Lab Details](http://education.planning.domains/lecturer_area/icaps20-ss-lab1.zip) |



- Publicly Available PDDL Domains
  - [IPC PDDL Domains](https://github.com/potassco/pddl-instances)
- Book: [An Introduction to the Planning Domain Definition Language](http://www.morganclaypoolpublishers.com/catalog_Orig/product_info.php?products_id=1384)

## ThePlanningCommunity

https://app.slack.com/plans/TK9TZPZD3?entry_point=team_messages_limit_meter&feature=unlimited_messages

Stack有一个planning community里面有很多资料


## Why MkDocs?

I like take notes with markdown opened by **Typora & Vnote** on my local PC notes system.

This document made by [mkdocs.org](https://www.mkdocs.org),because it can directly change my notes into wonderful help documents shown online.

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
