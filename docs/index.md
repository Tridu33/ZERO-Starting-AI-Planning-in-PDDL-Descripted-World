# 从零起步：PDDL 描述世界中的 AI 规划

> 凡事预则立，不预则废。本文档系统梳理 PDDL（规划领域定义语言）的核心概念、工具生态与前沿研究，为 AI 规划学习者提供一站式知识导航。

## 规划知识 Wiki

规划领域的主要在线知识库 [Planning.wiki](https://planning.wiki/) —— AI 规划与 PDDL 的权威 Wiki，涵盖从入门到精通的系统教程与参考资料。其源代码开源于 [planning-wiki](https://github.com/nergmada/planning-wiki)。

经典综述文献 [Everything You Always Wanted to Know About Planning (But Were Afraid to Ask)](https://fai.cs.uni-saarland.de/hoffmann/papers/ki11.pdf) 由 Jörg Hoffmann 撰写，系统回答了规划领域的核心问题。

来自 Universidad Simón Bolívar 的优质课程资料：[PF 3335 Artificial Intelligence Planning](https://yawgmoth.github.io/PF-3335/)，配套[课程项目](https://yawgmoth.github.io/PF-3335/project/)与[在线幻灯片](https://yawgmoth.github.io/PF-3335/slides/)。

## 学习资源

### 入门教程

- [Getting Started with PDDL](https://fareskalaboud.github.io/LearnPDDL/) —— 面向初学者的 PDDL 入门指南，系统讲解 PDDL 的基本语法与建模方法。源代码见 [LearnPDDL](https://github.com/fareskalaboud/LearnPDDL)。
- [PDDL Reference Guide](https://github.com/jan-dolejsi/pddl-reference) —— Jan Dolejsi 等人维护的 PDDL 语法参考手册，涵盖各版本规范的详细说明。
- [planning.wiki/extras](https://planning.wiki/extras) —— 规划工具与学习资源的精选合集。
- [PDDL 维基百科词条](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language#De_facto_official_versions_of_PDDL) —— 综述 PDDL 各版本语言特征与历史沿革。

### 视频教程

- [Learn PDDL by Fares K. Alaboud](https://fareskalaboud.github.io/LearnPDDL/)
- [Introduction to AI Planning. Part I. (video)](https://www.youtube.com/watch?v=EeQcCs9SnhU)
- [Introduction to AI Planning. Part II. (video)](https://www.youtube.com/watch?v=FS95UjrICy0)
- [VS Code PDDL 插件演示](https://www.youtube.com/watch?v=XW0z8Oik6G8)

### 中文社区资源

- [PDDL 知乎专栏](https://www.zhihu.com/column/pddl-basicnote) —— 中文世界系统介绍 PDDL 的学习专栏。
- [PDDL-editor——基于 VS Code 的简易规划器](https://zhuanlan.zhihu.com/p/113874556) —— 寻风者风寻撰写的 VS Code PDDL 入门文章。

### 规划社区

规划领域爱好者在 Slack 平台上设有 [The Planning Community](https://app.slack.com/plans/TK9TZPZD3?entry_point=team_messages_limit_meter&feature=unlimited_messages)，汇集了丰富的学术讨论与技术交流资源。

## Planning.Domains 生态系统

[Planning.Domains](http://planning.domains/) 是一个面向 AI 规划研究者的在线服务生态系统，由澳大利亚、西班牙、英国等多国研究机构联合构建。其核心组件包括：

### API 服务

[api.planning.domains](http://api.planning.domains/) 提供对 PDDL 基准领域及问题文件的编程访问接口。该 API 管理三类对象：

- **Problem（问题）**：涵盖每个问题的文件路径、对应领域、统计信息等。
- **Domain（领域）**：涵盖各领域的描述文档及统计指标。
- **Collection（集合）**：涵盖历届 IPC（国际规划大赛）的领域集合及特定规划器的集合。

经典规划领域的 PDDL 文件集合托管于 [classical-domains](https://github.com/AI-Planning/classical-domains)，研究者可通过克隆仓库或 API 命令行工具获取副本。目前接受经典 PDDL 基准（涵盖各版本与表现力层级），未来拟扩展至 POND、FOND、RDDL 等形式化体系。

### 在线求解器

[solver.planning.domains](http://solver.planning.domains/) 提供在线 PDDL 求解服务，支持通过 URL 链接或 JSON 格式提交原始 PDDL 内容，从而检索或验证规划方案。配套提供 JavaScript/Python 远程调用的示例代码。

### 在线编辑器

[editor.planning.domains](http://editor.planning.domains/) 集成 PDDL 编辑、求解与验证功能于一体，是基于 Web 的规划开发环境。

### 教育资源

[education.planning.domains](http://education.planning.domains/) 汇集自动化规划与建模的教学幻灯片、源代码及视频教程，是系统学习 AI 规划的优质起点。

## VS Code PDDL 扩展

VS Code 的 PDDL 扩展插件（[pddl](https://marketplace.visualstudio.com/items?itemName=jan-dolejsi.pddl)）是目前最成熟的 PDDL 开发环境，提供语法高亮、代码补全、规划器集成与验证等一站式功能。其源代码开源于 [vscode-pddl](https://github.com/jan-dolejsi/vscode-pddl)，示例工程见 [vscode-pddl-samples](https://github.com/jan-dolejsi/vscode-pddl-samples)。

插件集成了丰富的规划工具与资源：

- [VAL——规划验证器](https://nms.kcl.ac.uk/planning/software/val.html)：由 KCL 开发，依据原始领域与问题文件验证规划方案的正确性，在执行操作时确保全部前提条件得以满足，同时检验规划是否真正实现既定目标。
- [Eviscerator——规划器测试工具](https://www.github.com/nergmada/eviscerator)：自动测试并识别规划器所支持的 PDDL 需求特性，面向 Linux 提供预编译二进制文件。
- [ROSPlan——ROS 中的规划框架](https://github.com/KCL-Planning/ROSPlan/)：将 AI 规划集成至机器人操作系统（ROS），支持对机器人环境进行建模与任务规划执行。
- [Plansys2——ROS2 中的规划系统](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)：面向 ROS2 的规划集成框架，采用[行为树](https://github.com/BehaviorTree/BehaviorTree.CPP)实现动作执行，提供丰富[示例](https://github.com/IntelligentRoboticsLabs/ros2_planning_system_examples/)。
- [通用规划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)：由西班牙 UPF 研究团队主导开发，旨在支持经典、时序与多智能体规划的验证。

### 编辑器插件生态

除 VS Code 外，PDDL 还支持其他主流编辑器：

| 编辑器 | 插件 | 说明 |
|--------|------|------|
| Visual Studio Code | [PDDL Plugin for VSCode](https://marketplace.visualstudio.com/items?itemName=jan-dolejsi.pddl) | 功能最全面 |
| Sublime Text | [MyPDDL Plugin for Sublime](https://packagecontrol.io/packages/myPDDL) | 轻量级支持 |
| Atom | [MyPDDL Plugin for Atom](https://atom.io/packages/mypddl) | 已停止维护 |
| Web | [Planning.Domains PDDL Editor](http://editor.planning.domains/) | 在线编辑求解一体化 |

## 规划器工具集

### 经典规划器

- **Fast Downward** ([fast-downward.org](http://www.fast-downward.org/))：基于启发式搜索的经典规划系统，源代码见 [downward](https://github.com/aibasel/downward)。配套的 [Downward Lab](https://github.com/aibasel/lab) 提供实验评估框架，文档见 [lab.readthedocs.io](https://lab.readthedocs.io)。[planning.wiki 上的 Fast Downward 词条](https://planning.wiki/ref/planners/fd) 提供详细使用指南。
- **FF Planner** ([FF 官网](https://fai.cs.uni-saarland.de/hoffmann/ff.html))：由 Jörg Hoffmann 开发的经典前向启发式搜索规划器，曾获 IPC-2 杰出性能奖。
- **LAPKT** ([Lightweight Automated Planning Toolkit](https://lapkt-dev.github.io/docs/gettingStarted/))：轻量级自动规划工具包，集成多种启发式搜索算法。

### 通用规划器

- **MyND** ([GitHub](https://github.com/robertmattmueller/myND))：基于 Java 的启发式 AND/OR 搜索规划器。
- **PRP** ([planner-for-relevant-policies](https://github.com/QuMuLab/planner-for-relevant-policies))：基于经典重规划的 FOND 求解器。
- **FOND-SAT**：将 FOND 规划归约为 SAT 可满足性问题的求解方法。

### 领域实例集合

公开可用的 PDDL 领域实例：[IPC PDDL Domains](https://github.com/potassco/pddl-instances) —— 历届国际规划大赛使用的标准基准集。

推荐参考书籍：[An Introduction to the Planning Domain Definition Language](http://www.morganclaypoolpublishers.com/catalog_Orig/product_info.php?products_id=1384)，系统讲解 PDDL 的形式语义与建模实践。

## 课程与学术资源

### 教学幻灯片与课程

| 机构 | 课程内容 | 资源链接 |
|------|----------|----------|
| [UniBasel AI Group](https://ai.dmi.unibas.ch/) | AI 与规划课程 | [Lecture Slides](https://ai.dmi.unibas.ch/forstudents.html) |
| [FAI Group, Saarland University](http://fai.cs.uni-saarland.de/index.html) | AI 基础与规划课程 | [Lecture Slides](http://fai.cs.uni-saarland.de/teaching/), [Planning Source](http://education.planning.domains/lecturer_area/fai-planning.zip), [AI Source](http://education.planning.domains/lecturer_area/fai-ai.zip) |

### 教学实验与作业

| 课程/项目 | 负责人 | 说明 | 资源 |
|-----------|--------|------|------|
| [AI (CS) at PUCRS](https://github.com/pucrs-ai-cs) | Felipe Meneguzzi 等 | 基于启发式搜索的规划实验 | [Source Code](https://github.com/pucrs-automated-planning/heuristic-planning) |
| [Pacman Capture the Flag](https://ieeexplore.ieee.org/document/8468047) | Nir Lipovetzky, Sebastian Sardina | 基于 Berkeley AI Pacman 框架的竞赛 | [Competition](https://sites.google.com/view/pacman-capture-hall-fame), [Code](https://bitbucket.org/ssardina-teaching/pacman-contest/src/master/) |
| [ICAPS 2020 Summer School](https://icaps20subpages.icaps-conference.org/students/summer-school/icaps-online-summer-school-lab-plan-synthesis/) | Michael Cashmore | 使用 PDDL 进行规划建模的入门实验 | [Lab Details](http://education.planning.domains/lecturer_area/icaps20-ss-lab1.zip) |

