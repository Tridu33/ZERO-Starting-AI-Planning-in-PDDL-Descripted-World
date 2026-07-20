# PDDL 简介

[PDDL 版本语言特征 Wiki 介绍](https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language)

[DBLP 数据库 PDDL 相关研究文献](https://dblp.uni-trier.de/search?q=pddl) 可见该领域的研究现状备受学界关注，且其发展脉络自然地延伸至游戏编程领域中的人工智能行为树（Behavior Tree）——即"基于**行为树**的 PDDL 计划优化执行"（Optimized Execution of PDDL Plans using Behavior Trees），该概念在本质上与算法决策动作结构（decision structure）属同一范畴。

[Writing Planning Domains and Problems in PDDL](http://users.cecs.anu.edu.au/~patrik/pddlman/writing.html)

经典规划（classical planning）采用从 STRIPS 建模语言 [Richard E Fikes and Nils J Nilsson. STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving. *Artificial Intelligence*, 2(3-4):189–208, 1971] 派生而来的形式化描述语言，即规划领域定义语言（Planning Domain Definition Language, PDDL）[Drew McDermott, et al. PDDL—The Planning Domain Definition Language, 1998]。

本研究关注可满足（satisfying）的规划任务，其可由四元组 (F, O, I, G) 加以形式化定义，其中：F 为一组命题（或谓词），用于刻画任务实例中对象的属性及其相互关系；O 为一组算子（或称操作类型）；I ⊆ F 为初始状态；G ⊆ F 为目标状态集合。每个动作类型 o ∈ O 均由三元组 (Pre(o), Add(o), Del(o)) 定义，其中 Pre(o) 为前置信念集，代表操作适用所必须满足的谓词条件；Add(o) 为添加列表，代表操作执行后变为真的谓词集合；Del(o) 为删除列表，代表操作执行后变为假的谓词集合。本研究的核心目标在于寻找一个规划方案（plan），即一系列动作的有序序列，其依次应用后能够在有限时间步或预定步骤数内，将系统从初始状态 I 引导至目标状态 G 所涵盖的状态空间。

寻找规划任务的解通常依赖于启发式搜索方法。然而，本文的工作聚焦于学习反应式规划策略（reactive planning policies），此类策略可在特定领域的实例上进行训练，继而泛化至同一领域中未见过的全新实例。

## 人工智能规划语言视域下的 PDDL 与 Prolog

[Prolog 图灵机实现示例](https://www.metalevel.at/prolog/showcases/turing.pl)

概要：PDDL 是一种专用于表达规划任务的领域特定语言（domain-specific language），而 Prolog 则是一种成熟的通用编程语言，其表达能力覆盖所有可能的计算范畴，包括求解规划任务。

[Quora：PDDL 与 Prolog 表达能力差异探讨](https://www.quora.com/What-is-difference-in-expressive-power-between-PDDL-and-Prolog)

PDDL 全称为规划领域定义语言（Planning Domain Definition Language），是用于规划任务的标准编码规范。需注意，PDDL 存在多个版本，并衍生出各种扩展。

实际上，诸多标称为"PDDL"的求解器仅支持 PDDL 语言的若干子集。

通常，规划任务的描述由若干特定组件构成，例如：

> 初始状态（initial state）
> 目标条件（goal condition）
> 可执行动作（feasible actions）
> 等

若规划框架具备足够的通用性，则此类特定于领域的规划语言实际上可具备**图灵完备性（Turing-complete）**，从而与通用编程语言（如 Prolog）具有同等的计算能力：其理论依据在于，图灵机领域的建模可被视作一种经典的规划领域问题。

然而，PDDL 并非如此：在 PDDL 中，通常仅需对某些有限域（例如整数的有限区间）进行推理。由于域是有限的，PDDL 无法对无限磁带（infinite tape）进行建模，因此其表达能力**显著弱于** Prolog。

此外，研究者通常仅关注多项式长度的规划方案，甚至限定于此种约束之下。在此条件下，PDDL 属于 PSPACE 完全或 EXPTIME 完全问题，具体取决于所使用的扩展与变体。这尤其意味着**存在大量无法在 PDDL 框架内表达的计算任务**。

从实践角度审视，即便 PDDL 在理论上具备足够的表达能力以建模所有计算任务，在其预期规划应用领域之外使用是否便利或可取，仍值得深入商榷。因此，若欲借助 PDDL 描述自动机推演以生成策略（policy）算法控制流图解子图，从而实现"程序综合"（program synthesis），则可能需要依赖 PDDL 的扩展版本，或在其基础上构建若干框架（framework）。

另一方面，Prolog 是图灵完备的编程语言。这尤其意味着，任何能够在任意编程语言中表达的计算任务，均可以同样地在 Prolog 中加以表达。这一结论可通过在 Prolog 中模拟图灵机来加以证明。

## 在 PDDL 中编写规划领域和问题

以下是一些其他参考资料，希望对您有用：

[PDDL 入门教程（PDF）](https://www.cs.toronto.edu/~sheila/2542/s14/A1/introtopddl2.pdf)

[PDDL 1.2 语言手册（PDF）](http://homepages.inf.ed.ac.uk/mfourman/tools/propplan/pddl.pdf)

[In Defense of PDDL Axioms（PDF）](http://users.cecs.anu.edu.au/~thiebaux/papers/ijcai03.pdf)

[PDDL 在线编辑器](https://editor.planning.domains/#)
