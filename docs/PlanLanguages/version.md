以下内容摘录自 [automated-programming-framework](https://github.com/aig-upf/automated-programming-framework) 的作者 [Javier Segovia-Aguas](https://jsego.github.io/) 在其相关论文中对 PDDL 版本迭代历程的系统总结：

The Action Description Language (ADL) (Pednault, 1994) extended STRIPS allowing actions to have conditional effects, so some effects are triggered depending on the state. In contrast to STRIPS, ADL allows existential quantification, negative literals, goals with disjunctions, different object types, and while variables in STRIPS are either true or false, in ADL they can be true, false or undefined.

In the year 1998, with the aim to make a standard representation of planning languages, the Planning Domain Definition Language (PDDL) (McDermott et al., 1998) was published. The IPC has been used to compare planning solvers performance but also to include new features to the language. These are the different published versions:

- PDDL1.2 is the version used in the first international planning competition IPC-98 (Long et al., 2000) where the planning problem model is split into a domain and a problem description.

- PDDL2.1 (Fox and Long, 2003) introduced numeric fluents so resources can be represented. In previous versions, actions were directly applied in discrete time, but in this version actions can be described and performed in continuous space, so they are described as temporal or durative actions.
- PDDL2.2 (Edelkamp and Hoffmann, 2004) introduced derived predicates that can represent dependency among literals through transitive closures. This version also introduces timed initial literals where some literals are triggered by independent events at different times. 传递闭包机制使得描述更加精炼，适用于时序网络建模。
- PDDL3.0 (Gerevini and Long, 2006) introduced hard constraints called state-trajectory constraints that must be true along the execution of a plan, and soft constraints called preferences where plans that satisfy them are considered of better quality. 例如，软约束倾向于尽量少用 new ListNode 而直接以 O(1) 空间复杂度处理链表相关问题，或软链接倾向于以最少指令行数处理 goto 汇编代码的控制流程。
- PDDL3.1 introduced object-fluents where any function can be an object type. This feature is a reformulation of Functional STRIPS (Geffner, 2000).

定义 2.8（简洁性，Succinctness）。广义规划（generalized planning）的简洁性指的是解（solution）的规模大小。该规模可从多个维度加以度量，例如算法中已编程的代码行数、有限状态控制器（Finite State Controller, FSC）中的控制器数量、策略规则（policy rules）的条数等。

定义 2.9（复杂性，Complexity）。广义规划的复杂性是指关于描述规划实例输入变量的时间与空间函数的渐近分析。例如，计算复杂性理论中常使用大 O 符号（big-O notation）进行功能渐近分析与复杂性类别研究。
