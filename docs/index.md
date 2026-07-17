[TOC]

# ZERO-Starting AI Planning in PDDL-Descripted World

从零起步，于 PDDL-Descripted 世界之中，开启 AI 规划之探索征程。正所谓"凡事预则立，不预则废"，此之谓也。

## plan-wiki

https://github.com/nergmada/planning-wiki

https://fai.cs.uni-saarland.de/hoffmann/papers/ki11.pdf Everything You Always Wanted to Know About Planning (But Were Afraid to Ask)

人工智能规划领域之优质课程资料：https://yawgmoth.github.io/PF-3335/ PF 3335 Artificial Intelligence Planning 课程实践项目：https://yawgmoth.github.io/PF-3335/project/ 在线版教学幻灯片：https://yawgmoth.github.io/PF-3335/slides/

## Resources

**Tutorials**

Getting Started with PDDL：https://fareskalaboud.github.io/LearnPDDL/ 源码：https://github.com/fareskalaboud/LearnPDDL

https://github.com/jan-dolejsi/pddl-reference

https://planning.wiki/extras

https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language#De_facto_official_versions_of_PDDL

start-process-stop model.

marketplace.visualstudio.com/items?itemName=jan-dolejsi.pddl 相关教程资源

PDDL-editor（基于 VS Code 的简易规划器）——寻风者风寻所撰文章 - 知乎
https://zhuanlan.zhihu.com/p/113874556

https://www.zhihu.com/column/pddl-basicnote PDDL 知乎专栏

youtube.com/watch?v=XW0z8Oik6G8

相关网站资源

https://planning.wiki/（GitHub 上提供完整源代码）https://github.com/nergmada/planning-wiki

https://github.com/jan-dolejsi/pddl-reference/tree/master/docs 关于 PDDL 语言、规划方法、历史沿革、具体用法及研究进展之详尽阐述，敬请参阅该指南。

视频教程资源：

  - [Learn PDDL by Fares K. Alaboud](https://fareskalaboud.github.io/LearnPDDL/)
  - [Introduction to AI Planning. Part I. (video)](https://www.youtube.com/watch?v=EeQcCs9SnhU)
  - [Introduction to AI Planning. Part II. (video)](https://www.youtube.com/watch?v=FS95UjrICy0)

http://planning.domains/

api.planning.domains

solver.planning.domains

开源项目源代码
github.com/jan-dolejsi/vscode-pddl

github.com/jan-dolejsi/vscode-pddl-samples

## VS Code PDDL 扩展插件

VS Code 的 PDDL 扩展插件汇聚了众多相关研究资源与学术链接。

VS Code 插件 PDDL：AI Planning and PDDL support in VS Code

youtube.com/watch?v=XW0z8Oik6G8&feature=youtu.be

Below you can find a collection of resources for writing, learning and using PDDL and planning. For more information on what these tools and resources are and how they can help, please visit the [additional resources](https://github.com/nergmada/planning-wiki/blob/master/extras) page.

- [Planning.Domains](http://planning.domains/)
- Planner Tools
  - [VAL - The Plan Validator](https://nms.kcl.ac.uk/planning/software/val.html)
  - [ROSPlan - Planning in ROS](https://github.com/KCL-Planning/ROSPlan/)
  - [PlanSys2 - Planning in ROS2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)
  - [Eviscerator - The Planner tester](https://www.github.com/nergmada/eviscerator)
  - [Universal Planning Validator (Under Development)](https://github.com/aig-upf/universal-planning-validator)

https://planning.wiki/extras 详细介绍

## solver.planning.domains：在线规划解决方案

http://solver.planning.domains/

http://planning.domains/

包括：

- api
  http://api.planning.domains/ API 查询

https://github.com/AI-Planning/classical-domains PDDL 文件的系统化集合，当前仅涵盖经典规划问题。

planning.domains API 提供了对广泛 PDDL 基准领域及问题文件的编程访问能力。所有底层物理文件均可于 GitHub 的域存储库中找到。研究者既可通过克隆存储库获取副本，亦可借助下文所述之命令行实用工具自行获取。

如在 PDDL 文件中发现任何错误（如集合不完整、定义不当等），请克隆存储库，并将修订内容以 Pull Request 形式提交。在合理范围内，本团队亦接受包含全新基准测试集的 Pull Request（例如于新一届 IPC 竞赛之后，或作为特定领域套件之发布）。目前仅接受经典 PDDL 基准（涵盖任意 PDDL 级别与表现力），然未来我们企望将其扩展至更丰富的其他形式化体系（如 POND、FOND、RDDL 等）。

文件集合仅是 api.planning.domains 的首个组件。该服务的核心功能在于提供查询、浏览及审视现有领域的交互式界面。我们持续存储并更新每一领域及问题之各类属性，诸如规划成本之上界与下界、领域中的需求约束、问题的经典宽度等。在此页面上，您可查阅 api.planning.domains 接口之描述，以及用于简化 API 交互的相关工具与程序库之详细信息。

该 API 包含三种类型的对象：

- Problem（问题）：涵盖每个问题的信息，包括其文件、对应的领域文件、问题统计信息等。
- Domain（领域）：涵盖每一单独领域之信息，包括其描述及该领域的各项统计指标。
- Collection（集合）：涵盖领域集合，包括历届 IPC 的集合、单个规划程序集合等。

免责声明：目前，该 API 尚处于高度 Alpha 阶段。期望最终能有一种精确引用评估软件所用基准之方法，但目前我们仍在修复领域、替换问题集并纠正各项统计数据之错误。在移除本免责声明之前，建议您勿将 API 用于正式事务（涵盖学术界及其他领域）。

- solver

http://solver.planning.domains/

在线 PDDL 文件求解器之使用示例教程：

可通过发送指向 PDDL 文件的链接，或直接以 JSON 格式提交原始 PDDL 内容来调用该求解器，从而检索或验证规划方案。

Javascript/Python 远程调用之使用范例与代码

- editor

http://editor.planning.domains/ 在线 PDDL 编辑器、求解器与验证器

- education

http://education.planning.domains/

学习自动化规划与建模技术的优质资源

教学幻灯片、源代码及视频教程

## 规划工具集锦

 [VAL——规划验证器](https://nms.kcl.ac.uk/planning/software/val.html)

[VAL](https://nms.kcl.ac.uk/planning/software/val.html)（亦称验证器）是一种用于依据原始领域与问题文件验证规划器所生成解决方案的工具。VAL 可在执行操作时确保规划所需之全部前提条件得以满足，同时检验规划是否真正实现了既定目标。

 [Eviscerator——规划器测试工具](https://www.github.com/nergmada/eviscerator)

[Eviscerator](https://www.github.com/nergmada/eviscerator) 是为本 PDDL 参考指南而开发的工具，其能够自动测试并识别规划器所支持的 PDDL 需求。作为一款开源工具，它随附面向 Linux 的持续部署预构建二进制文件，研究者可直接下载并测试规划器，无需操心编译流程。

 [ROSPlan——ROS 中的规划框架](https://github.com/KCL-Planning/ROSPlan/)

[ROSPlan](https://github.com/KCL-Planning/ROSPlan/) 是机器人操作系统（ROS）的一个模块，旨在将 AI 规划集成至基于 ROS 的机器人系统之中。ROSPlan 支持对机器人环境进行建模，以规划和执行各类任务。

[Plansys2——ROS2 中的规划系统](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)

[Plansys2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system) 是机器人操作系统新版本——**ROS2** 中的重要项目，致力于整合规划与机器人技术。其目标在于构建一个框架，使得不同的规划器能够轻松集成，从而驱动机器人执行各项任务。系统采用[行为树](https://github.com/BehaviorTree/BehaviorTree.CPP)实现[动作](https://github.com/BehaviorTree/BehaviorTree.CPP)，仓库中亦提供了丰富的[示例](https://github.com/IntelligentRoboticsLabs/ros2_planning_system_examples/)。

 [通用规划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)

[通用规划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator) 是一种用于验证规划领域与问题的工具。目前，它仅支持经典规划问题与领域，但该工具的设计目标在于未来扩展至时间域与多主体域。如需支持比传统规划更丰富的 PDDL 高级功能之验证器，建议使用 VAL（规划验证器）替代。

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
| [Pacman Capture the Flag in AI Courses](https://ieeexplore.ieee.org/document/8468047) | Nir Lipovetzky, Sebastian Sardina                           | Competition using the Berkley AI Pacman framework. Students use search algorithms, PDDL, classical replanning, minimax, etc. for their agents. | [Competition](https://sites.google.com/view/pacman-capture-hall-fame) [Code](https://bitbucket.org/ssardina-teaching/pacman-contest/src/master/) |
| [ICAPS 2020 Summer School Plan Synthesis](https://icaps20subpages.icaps-conference.org/students/summer-school/icaps-online-summer-school-lab-plan-synthesis/) | Michael Cashmore                                            | This training lab is an introduction to modelling planning problems using the Planning Domain Definition Language (PDDL). | [Lab Details](http://education.planning.domains/lecturer_area/icaps20-ss-lab1.zip) |



- Publicly Available PDDL Domains
  - [IPC PDDL Domains](https://github.com/potassco/pddl-instances)
- Book: [An Introduction to the Planning Domain Definition Language](http://www.morganclaypoolpublishers.com/catalog_Orig/product_info.php?products_id=1384)

## ThePlanningCommunity

https://app.slack.com/plans/TK9TZPZD3?entry_point=team_messages_limit_meter&feature=unlimited_messages

Stack 平台上设有一个 Planning Community，其中汇集了丰富的学术资源与讨论资料。


## Why MkDocs?

I like take notes with markdown opened by **Typora & Vnote** on my local PC notes system.

This document made by [mkdocs.org](https://www.mkdocs.org), because it can directly change my notes into wonderful help documents shown online.

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
