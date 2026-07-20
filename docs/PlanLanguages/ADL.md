# 动作描述语言（Action Description Language, ADL）

## ADL 概述

动作描述语言（Action Description Language, ADL）由 Pednault 于 1994 年提出，是对 STRIPS 形式化框架的重要扩展。ADL 允许动作具有条件效果（conditional effects），即某些效果根据当前状态的条件触发而生效。与 STRIPS 相比，ADL 引入了以下关键表达能力：

- **存在量化（existential quantification）**：允许在动作描述中使用存在量词。
- **负文字（negative literals）**：支持在条件与效果中使用否定形式。
- **析取目标（goals with disjunctions）**：目标条件可包含逻辑或关系。
- **多对象类型（different object types）**：支持类型化变量，增强了领域建模的灵活性。
- **三值逻辑**：STRIPS 中变量取值仅为真（true）或假（false），而 ADL 中变量可取真、假或未定义（undefined）三种状态。

## ADL 与 PDDL 的关系

1998 年，为建立统一的规划语言标准，规划领域定义语言（Planning Domain Definition Language, PDDL）（McDermott et al., 1998）正式发布。PDDL 在设计上吸收了 ADL 的诸多表达能力，并将其融入标准化的语言框架之中。国际规划竞赛（International Planning Competition, IPC）不仅是比较各类规划求解器性能的平台，也推动了 PDDL 语言特性的持续扩展。

PDDL 的后续版本在 ADL 的基础上进一步引入了数值流利（numeric fluents）、派生谓词（derived predicates）、时序动作（durative actions）、状态轨迹约束（state-trajectory constraints）与软约束偏好（preferences）等高级特性，从而覆盖了从简单 STRIPS 表示到复杂时间规划与资源优化的广泛表达能力谱系。
