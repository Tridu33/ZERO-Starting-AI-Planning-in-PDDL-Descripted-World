
# Planner Tools

- [VAL - The Plan Validator](https://nms.kcl.ac.uk/planning/software/val.html)
- [ROSPlan - Planning in ROS](https://github.com/KCL-Planning/ROSPlan/)
- [PlanSys2 - Planning in ROS2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)
- [Eviscerator - The Planner tester](https://www.github.com/nergmada/eviscerator)
- [Universal Planning Validator (Under Development)](https://github.com/aig-upf/universal-planning-validator)



https://planning.wiki/extras 规划工具介绍

 [VAL-计划验证器](https://nms.kcl.ac.uk/planning/software/val.html)

[VAL](https://nms.kcl.ac.uk/planning/software/val.html)（亦称验证器）是一种用于验证规划器所生成之解决方案的权威工具，其验证依据为原始的领域定义文件与问题定义文件。该工具确保在执行动作序列时，所有规划所需的前提条件均得以满足，并严格检验规划是否真正实现了预定义的目标状态。

 [Eviscerator-规划器测试器](https://www.github.com/nergmada/eviscerator)

[Eviscerator](https://www.github.com/nergmada/eviscerator)是为本PDDL参考指南所开发之专用工具，可用于自动测试并识别规划器所支持的PDDL需求特性。该项目为开源实现，提供面向Linux持续集成与部署流程的预编译二进制文件。研究者可直接下载并测试规划器，无需自行执行编译过程。

 [ROSPlan-ROS中的规划](https://github.com/KCL-Planning/ROSPlan/)

[ROSPlan](https://github.com/KCL-Planning/ROSPlan/)是机器人操作系统（ROS）框架下的一个核心功能模块，旨在将AI规划能力无缝集成至基于ROS的机器人系统中。ROSPlan支持对机器人运行环境进行形式化建模，从而实现任务层面的规划与执行。

[Plansys2-在ROS2中进行规划](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)

[Plansys2](https://github.com/IntelligentRoboticsLabs/ros2_planning_system)是面向新一代机器人操作系统 **ROS2** 的项目，旨在深度整合规划理论与机器人技术。其核心目标在于构建一个能够灵活集成多种规划器的通用框架，以支持机器人执行多样化的复杂任务。动作的实现基于[行为树](https://github.com/BehaviorTree/BehaviorTree.CPP)，仓库中亦提供了丰富的实践[示例](https://github.com/IntelligentRoboticsLabs/ros2_planning_system_examples/)。

 [通用规划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)

[通用规划验证器（开发中）](https://github.com/aig-upf/universal-planning-validator)是一种用于验证规划领域与问题的通用工具。当前版本仅支持经典规划问题与领域，但其设计目标在于逐步扩展至时间规划领域与多智能体规划领域。若需支持超越经典规划的PDDL高级语言特性，建议使用VAL（规划验证器）作为替代方案。



https://github.com/aig-upf/universal-planning-validator 西班牙研究团队亦深度参与了该项目的研发工作


https://github.com/KCL-Planning/VAL

https://planning.wiki/extras

https://github.com/patrikhaslum/INVAL






