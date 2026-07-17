




# qnp2ast2program

一个QNP（Qualitative Numeric Planning）问题本质上构成一个AOV网络（Activity-on-Vertex Network），类似于迁移系统（Transition System），其策略（Policy）定义了从状态到动作的映射关系。这一范式与图灵机模型在算法表示层面具有结构上的相似性。

模型检测（Model Checking）试图以诸如ATL*（Alternating-time Temporal Logic）之类的逻辑语言来描述此类系统。然而在实际研究中，大量文献采用FOND（Fully Observable Non-Deterministic）框架进行建模，其原因在于FOND相对易于处理。尽管如此，或许有必要探索一种全新的逻辑体系以更精准地刻画QNP问题的本质特性。


1. QNP

```pddl
domain.pddl
probelm_p.pddl
```


2. MyND类规划器及其改进型GraphPlanner



2. 解图（Solution Graph）——数据流控制图（Data Flow Controller Chart）



2. 抽象语法树（AST）



2. 程序生成（Program）


阅读QNP原始论文：
LL领域规划问题  ---> 链表程序问题（Linked List Program Problem）


扩展LL领域（Extended LL Domain）

![Extended LL Domain](_v_images/20210119163854008_12530.png)

```c
C++、Java等模板元编程技术，生成器（Generator）
```

- 命令式编程语言（Imperative Programming Language）
解析树（Parser Tree） LLVM中间表示（IR） C风格程序


- Coq提取（Coq Extraction）
函数式问题：OCAML / HASKELL
Why工具

6. 依据编译原理的相关知识，在对解析器（Parser）生成的抽象语法树（AST）进行处理时，需进行”类型检查”与”有效性分析”。当前学术界已存在针对程序终止性进行判定与测试的软件工具。
   可借鉴IC3 / nuSMV形式化验证领域的多项技术，对包含分支与循环的程序进行形式化验证与终止性分析。https://zybuluo.com/sangyy/note/128535


- 分支方向一：强化学习求解器与规划环境的交互通信，如同pddlgym项目所构建的范式，是否可类比构建qnpgym？**在AOV网络中寻找一条可行的路径。**
**

下图可被改造为经典的Gripper问题示例
![rl+qnp](_v_images/20210119163320407_24816.png)
马尔可夫过程具有无记忆性（Memoryless Property），即状态到动作的映射关系（state --> action）。

现有文献已实现具有记忆能力的轨迹到动作映射（trajectory --> action），其中记忆变量对应QNP中的数值变量。代表性工作如《Reinforcement Learning with Non-Markovian Rewards》。

近年来，将深度学习方法应用于规划问题求解已成为一个重要的研究方向，详见2020年ICAPS会议主页。
https://icaps20subpages.icaps-conference.org/workshops/prl/
>从概率推理的角度理解强化学习和控制(一） - stone的文章 https://zhuanlan.zhihu.com/p/339881664
Generalized Planning with Deep Reinforcement Learning 
Symbolic Plans as High-Level Instructions for Reinforcement Learning
Learning Neural Search Policies for Classical Planning
近年来，将深度学习方法应用于求解规划问题的研究已日益涌现。
学术界曾普遍认为确定性策略的强化学习（Deterministic Policy RL）并不存在，直至2014年Silver等人在《Deterministic Policy Gradient Algorithm》中提出确定性策略梯度方法。
2015年，DeepMind将深度Q网络（DQN）与确定性策略梯度相结合，提出了DDPG算法（Continuous Control with Deep Reinforcement Learning）。

- 分支方向二：Isabelle / Coq辅助定理证明系统，通过”推理”手段判定程序终止性，结合模型检测（Model Checking）技术，构建软件系统可信性验证框架。

- 逻辑公式演算与谓词逻辑天然形成类似Golog的逻辑式命令式程序，运行于Prolog推理引擎之上。
- 逻辑公式演算亦天然适用于生成OCAML等”函数式编程语言”，这方面的具体实现包括Coq的Extraction机制。
- 领域特定语言（DSL）可借助编译原理前端的”语法分析与词法分析”形成中间表示，进而通过AST等价转换为C风格程序。（此方向目前尚缺乏公开的学术论文加以探索。）

































