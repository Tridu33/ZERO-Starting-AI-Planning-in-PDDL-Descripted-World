写出[automated-programming-framework](https://github.com/aig-upf/automated-programming-framework)的[Javier Segovia-Aguas](https://jsego.github.io/)在相关论文中总结过PDDL的版本迭代情况：

The Action Description Language (ADL) (Pednault, 1994) extended STRIPS al-lowing actions to have conditional effects, so some effects are triggered depending on the state.  In contrast to STRIPS, ADL allows existential quantification, negative literals, goals with disjunctions, different object types, and while variables in STRIPS are either true or false, in ADL they can be true, false or undefined.

In the year 1998, with the aim to make a standard representation of planning languages, the Planning Domain Definition Language (PDDL) (McDermott et al.,1998) was published. The IPC has been used to compare planning solvers performance but also to include new features to the language.  These are the different published versions:

- PDDL1.2is the version used in the first international planning competition IPC-98 (Long et al., 2000) where the planning problem model is splitted into a domain and a problem description.-  

- PDDL2.1(Fox and Long, 2003) introduced numeric fluents so resources can be represented.  In previous versions, actions were directly applied indiscrete time, but in this version actions can be described and performed in continuous space, so they are described as temporal or durative actions.
- PDDL2.2(Edelkamp and Hoffmann, 2004) introduced derived predicates that can represent dependency among literals through transitive closures. This version also introduces timed initial literals where some literals are triggered by independent events at different times.传递闭包，描述更加精炼。时序网络建模。
- PDDL3.0(Gerevini  and  Long,  2006)  introduced  hard  constraints  called state-trajectory constraints that must be true along the execution of a plan,and  soft  constraints  called preferences where  plans  that  satisfy  them  are considered of better quality.比如软约束尽量少new ListNode直接用O(1)空间复杂度处理链表类似于相关问题，或者软链接希望处理goto汇编代码控制流程指令行数尽量少。
- PDDL3.1 introduced object-fluents where  any  function  can  be  an  object type. This feature is a reformulation of Functional STRIPS(Geffner, 2000).



定义2.8（简洁）。广义计划的简洁性是解\ n \的大小。大小可以度量为算法中已编程的行数，FSC中的控制器数，策略规则的数量等等。

定义2.9（复杂性）。广义计划的复杂性是关于用于描述计划实例的输入变量的时空函数的渐近分析。例如，在计算复杂性理论中使用big-O符号进行功能分析和复杂性类的研究。



