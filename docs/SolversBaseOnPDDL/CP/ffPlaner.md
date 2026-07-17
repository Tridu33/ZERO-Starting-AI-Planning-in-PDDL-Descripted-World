[TOC]

https://github.com/pucrs-automated-planning/pddl-parser Classical Planning in Python

- [PDDL.py](https://github.com/pucrs-automated-planning/pddl-parser/blob/master/PDDL.py) 提供了 PDDL 解析器
- [planner.py](https://github.com/pucrs-automated-planning/pddl-parser/blob/master/planner.py) 提供了规划器

# ffPlaner

在线编辑与求解 FF Planner：http://editor.planning.domains/#      

请注意，应避免使用 HTTPS 协议进行访问，否则将引发 malformed URL 错误。

http://www.ai.mit.edu/courses/16.412J/ff.html  大学教程链接，其中包含一个 tireworld 轮胎更换域实例：

> ff -o tyreworld_domain.pddl -f tyreworld_facts1


https://fai.cs.uni-saarland.de/hoffmann/ff.html FF 官方下载主页

FF 规划器是智能规划领域中最具盛名的成果之一。它采用经典的前向搜索方法，并结合启发式算法，显著提升了规划算法的搜索效率，在历届国际规划大赛中均取得了优异的成绩。

下载镜像：http://www.pudn.com/Download/item/id/2027550.html

使用方法：在 ff 可执行文件所在目录下执行以下命令：


```
./ff -o ./ff-domains/domain.pddl -f ./ff-domains/data.pddl
```


此外，也可将 ff 复制至 /usr/local/bin 目录下，执行命令为 `sudo cp ff /usr/local/bin`，之后仅需在命令行中输入：

```
ff -o ./ff-domains/domain.pddl -f ./ff-domains/data.pddl
```


演示示例


更多示例可参见以下资源：

http://fai.cs.uni-saarland.de/hoffmann/ff-domains.html 该页面由 Joerg Hoffmann 创建，是致力于开展大规模规划实证研究的重要起点。FF 域集合为 20 个 STRIPS 与 ADL 规划基准域提供（可能的）生成器，其中涵盖了两项竞赛所使用的示例。下文针对每个域，提供关于其起源、所进行的调整（如有）、生成器参数以及随机化策略的详细信息。可以下载域文件和生成器的 C 源代码。单击[此处](http://fai.cs.uni-saarland.de/hoffmann/ff-domains.tgz)下载整个软件包。关于如何生成（包括 makefile）以及如何运行，生成器应当是不言自明的。在不太直观的情况下，还随附了 README 文件以供参考。

Ubuntu 系统运行 FF-planner 


```
Ubuntu 18.04.2 LTS

Prerequisit:
1. change to software source to Tsinghua source.
2. sudo apt-add-repository ppa:swi-prolog/stable
3. sudo apt-get update
4. sudo apt-get install python3-pip
5. sudo apt-get install flex

Installation:
1. Download z3 from https://github.com/Z3Prover/z3
2. python3 scripts/mk_make.py
3. cd build
4. make
5. sudo make install
6. sudo apt-get install swi-prolog
7. sudo pip3 install pyswip 
8. Download FF-planner from http://fai.cs.uni-saarland.de/hoffmann/ff.html
9. make
```


报错

```
gcc -c -Wall -g -std=gnu99    -O6 inst_hard.c
gcc -c -Wall -g -std=gnu99    -O6 inst_final.c
gcc -c -Wall -g -std=gnu99    -O6 orderings.c
gcc -c -Wall -g -std=gnu99    -O6 relax.c
gcc -c -Wall -g -std=gnu99    -O6 search.c
flex -Pfct_pddl lex-fct_pddl.l
bison -pfct_pddl -bscan-fct_pddl scan-fct_pddl.y
make: bison: Command not found
makefile:78: recipe for target 'scan-fct_pddl.tab.c' failed
make: *** [scan-fct_pddl.tab.c] Error 127
```

安装 bison 工具即可解决此问题。

## Planning Domain Definition Language

基本内容：

•	Domain Name
•	Requirements
•	Types
•	Constants
•	Domain Variables
•	Predicates
•	Actions



- spare tire


domain_spare_tire_d.pddl


```pddl
；给出domain名称，语法使用就是(domain 名称)
(define (domain spare_tire )
   ;给出依赖项，比如这里的三个都是依赖项，语法使用是":依赖项",
   ;strip---The most basic subset of PDDL, consisting of STRIPS only
   ;equality---This requirement means that the domain uses the predicate =, interpreted as equality.
   ;typing---This requirement means that the domain uses types (see Typing below).
   ;adl---Means that the domain uses some or all of ADL (i.e. disjunctions and quantifiers in preconditions and goals, quantified and conditional effects).
   (:requirements : strips : equality : typing )
   (:types physob location )
   ；定义该domain当中需要使用的类型，比如physic object、location都是类型，直接将你需要定义的类型加入到:type的后面
   (:predicates  ( Tire ?x − physob)
                  ( at ?x − physob ?y − location ))
   ；定义该domain需要使用的谓词，单元谓词表示属性，如这里的Tire x表示x这个physic object是否有轮胎属性。
   ；谓词名称最先给出，然后依次给出该谓词的项，格式为"?参数 – 参数类型"，
   ；比如这里的"?x – physob ?y – physob"表示x这个参数的类型应该是physob的，不能传递其他类型的参数。
   ；整个"Tire ?x – physob"对应Tire(x)这一原子（公式）。
   ；二元谓词表示关系，比如这里的at表示x物体是否在y这个位置，分析与上面的单元谓词类似


    (:action Remove
    :parameters (?x − physob ?y − location )
    :precondition (At ?x ?y)
    :effect (and(not(At ?x ?y) ) (At ?x Ground) )
    )
    ;定义该domain中的操作，这里的remove表示移除操作，这个操作需要给定参数，参数定义规则与前面的谓词一样；
    ;action执行需要一定的前提条件，前提条件是一个逻辑表达式，
    ;根据其真值判断操作是否可以执行；
    ;最后执行这个操作会导致一定的结果，这在effect中指定，指定的effect会改写当前状态（相当于改写知识库中基础原子的真值）
    ;语法上来说，precondition后面可以给出原子公式的与或非组合，
    ;其中原子公式语法前面谓词说过了，非：（not 原子公式）；与：（and 原子公式1 原子公式2 等等）；或与and用法一致，把and换为or即可


    (:action PutOn
    :parameters (?x − physob)
    :precondition (and( Tire ?x) (At ?x Ground)
                   (not(At Flat Axle) ) )
    :effect (and(not(At ?x Ground) ) (At ?x Axle) ) 
    )

    (:action LeaveOvernight
    :effect (and(not(At Spare Ground) ) (not(At Spare Axle) )
             (not(At Spare Trunk) ) (not(At Flat Ground) )
             (not(At Flat Axle) ) (not(At Flat Trunk) )
             )
    )

)
```

spare_tire_p.pddl
```pddl
 (define (problem prob)
  (:domain spare_tire )
  (:objects Flat Spare −physob Axle Trunk Ground − location )
  (:init ( Tire Flat ) ( Tire Spare) (At Flat Axle) (At Spare Trunk) )
  (:goal (At Spare Axle) )
 )
```

- briefcase world

forall 与 when 的用法。本节首先阐释该 domain 的语义内涵，继而展示 forall 与 when 的具体用法。

briefcase_d.pddl

```pddl
(define (domain briefcase)
    (:requirements :strips :equality :typing :conditional-effects)
    (:types location physob)
    (:constants B - physob)
    (:predicates (at ?x - physob ?l - location) (in ?x - physob))
    (:action mov-b
        :parameters (?m ?l - location)
        :precondition (and (at B ?m) (not (= ?m ?l)))
        :effect (and (at B ?l) (not (at B ?m))
                    ;注意到写在effect中的这段代码：
                    (forall (?z - physob)
                        (when (and (in ?z) (not (= ?z B)))
                            ;这里意思就是遍历所有的object z，当z在B中，就产生effect
                            ;即将z的位置location设置为l（因为z在briefcase当中，briefcase被携带到了l地点，那么z自然也被移动到l）
                            (and (at ?z ?l) (not (at ?z ?m)))
                            ;这里必须使用forall，因为你无法设置是哪个对象在briefcase中，所以需要遍历判断
                        )
                    )
                ) 
    )
    (:action put-in
        :parameters (?x - physob ?l - location)
        :precondition (not (= ?x B))
        :effect (when (and (at ?x ?l) (at B ?l))
            (in ?x)) 
    )
    (:action take-out
        :parameters (?x - physob)
        :precondition (not (= ?x B))
        :effect (not (in ?x))
    )
)

```

然后给出数据文件，对该问题进行定义，其内容包括：

所涉及的 domain、
问题的参数定义、
问题的初始状态、
问题的目标状态。

完成问题定义后，调用求解器即可获得一系列 action，使问题从初始状态演变为目标状态（若解存在）。


briefcase_p.pddl
```pddl
(define (problem get-paid)
    (:domain briefcase)
    (:objects P D -physob home office - location)
    (:init 
        (at B home) (at P home) (at D home) (in P)
    )
    (:goal (and (at B office) (at D office) (at P home)))
)

```

- 8-puzzle

domain_puzzle_d.pddl
```pddl
; Header  and  description
( define (domain puzzle )
    ; remove  requirements  that  are  not  needed
    (:requirements :strips :typing :conditional−effects :equality )
    (:types
    ;todo: enumerate types and their hierarchy here,e.g. car truck bus − vehicle
    num loc
    )
    ;un−comment  following   line  if  constants   are  needed
    ;( :constants  )
    (:predicates
    ; todo:   define  predicates  here
        ( at ?x − num ?y − loc )
        ( adjecent ?x − loc ?y − loc )
    )
    ;(:functions; todo:   define numeric  functions   here
    ;)
    ;define  actions   here
    (:action slide
        :parameters (?x − num ?y − loc ?z − loc )
        :precondition (and( at ?x ?y) ( at num0?z) ( adjecent ?y ?z) )
        :effect (and( at ?x ?z) ( at num0 ?y) (not( at ?x ?y) ) (not( at num0?z) ) )
    )
)    
```


domain_puzzle_p.pddl
```pddl
(define (problem prob) (: domain puzzle )
    (: objects
        num0 num1 num2 num3 num4 num5 num6 num7 num8 − num
        loc1 loc2 loc3 loc4 loc5 loc6 loc7 loc8 loc0 − loc
    )
    (: init
        ; todo:   put  the   initial   state ' s   facts  and  numeric  values  here
        ( at num1 loc1 ) ( at num2 loc2 ) ( at num3 loc3 )
        ( at num7 loc4 ) ( at num8 loc5 ) ( at num0 loc6 )
        ( at num6 loc7 ) ( at num4 loc8 ) ( at num5 loc0 )
        ( adjecent loc1 loc2 ) ( adjecent loc2 loc1 )
        ( adjecent loc1 loc4 ) ( adjecent loc4 loc1 )
        ( adjecent loc2 loc3 ) ( adjecent loc3 loc2 )
        ( adjecent loc2 loc5 ) ( adjecent loc5 loc2 )
        ( adjecent loc3 loc6 ) ( adjecent loc6 loc3 )
        ( adjecent loc4 loc5 ) ( adjecent loc5 loc4 )
        ( adjecent loc4 loc7 ) ( adjecent loc7 loc4 )
        ( adjecent loc5 loc6 ) ( adjecent loc6 loc5 )
        ( adjecent loc5 loc8 ) ( adjecent loc8 loc5 )
        ( adjecent loc6 loc0 ) ( adjecent loc0 loc6 )
        ( adjecent loc7 loc8 ) ( adjecent loc8 loc7 )
        ( adjecent loc8 loc0 ) ( adjecent loc0 loc8 )
    )

    (: goal (and
        ; todo:   put  the   goal  condition   her e
        ( at num1 loc1 ) ( at num2 loc2 ) ( at num3 loc3 )
        ( at num4 loc4 ) ( at num5 loc5 ) ( at num6 loc6 )
        ( at num7 loc7 ) ( at num8 loc8 ) ( at num0 loc0 )
        ) 
    )

    ; un−comment  the   following   line  if  metric  is  needed
    ; ( : metric minimize  ( ? ? ? ) )
)

```

- blockworld

There are a collection of blocks: a block can be on the table, or on the top of another block.

There are three predicates

•clear(x): there is no block on top of block x;

•on(x,y): block x is on the top of block y;

•onTable(x): block x is on the table

There are two actions in this task:

•move(x,y): move block x onto block y, provided that both x and y are clear;

•moveToTable(x): move block x on to the table, provided that x is clear and x is not on thetable;


Give initial state and goal state, find the actions change the initial state to the goal state.

domain_blocks_d.pddl

```pddl
; Header  and  description
( define (domain blocks )
    ;remove  requirements  that  are  not  needed
    (:requirements :strips :typing :conditional−effects :equality :universal−preconditions : negative−preconditions )
    (:types
        ; todo: enumerate types and their  hierarchy here , e.g. car truckbus  −  vehicle
        physob
    )

    ;un−comment following  line  if constants are  needed
    ;( :constants  )

    (:predicates; todo: define  predicates here
        (ontable ?x − physob)
        (clear ?x − physob)
        (on ?x ?y − physob)
    )

    ;(:functions; todo:define numeric functions here
    ;)

    ;define actions here
    (:action move
        :parameters (?x ?y − physob)
        :precondition (and( clear ?x) ( clear ?y) )
        :effect (and(on ?x ?y) (not( clear ?y) )
            (when( ontable ?x) (not( ontable ?x) ) )
            (forall (?z − physob) (when(on ?x ?z) (and(not(on ?x ?z) ) (clear ?z) ) ) )
        )
    )

    (:action moveToTable
        :parameters (?x − physob)
        :precondition (and( clear ?x) (not( ontable ?x) ) )
        :effect (and(not( clear ?x) ) ( ontable ?x)
        ( forall (?z − physob) (when(on ?x ?z) (and(not(on ?x ?z) ) (clear ?z) ) ) )
        )
    )
)
```


domain_blocks_p.pddl
```pddl
(define (problem prob) (:domain blocks)
    (:objects
        A B C D E F − physob
    )
    (:init
        ; todo :put  the   initial   state ' s   facts  and  numeric  values   here
        (clear A) (on A B) (on B C) (ontable C) (ontable D)
        (ontable F) (on E D) (clear E) (clear F)
    )
    (:goal (and
        ; todo :   put  the   goal   condition   here
        (clear F) (on F A) (on A C) (ontable C) (clear E)
        (on E B) (on B D) (ontable D)
        )
    )
    ;un−comment  the   following   line   if   metric   is   needed
    ;(:metric  minimize  ( ? ? ? ) )
)

```

FF 规划器并不能保证生成最优方案。例如，在 Puzzle 问题中即出现了连续拨动数字 6 的情况，经手动验证，两个问题的规划结果（Plan）均是正确的。（注：代码中的注释由 Vscode 插件自动生成）

--------------------------------------------------------------------------------------------------------------------------

**>>规划基准中的本地搜索拓扑**

FF 的性能引出了一个极具启发性的问题：*为什么*它在如此众多的领域中表现优异？启发式算法（尤其是局部搜索算法）的成功，在很大程度上取决于其所采用的启发式函数的质量，亦即取决于使用该启发式函数进行评估的底层搜索空间的*局部搜索拓扑*，这一点已成为学术界的共识。因此，问题的关键在于：*在 FF 表现出色的那些领域中，其搜索空间具备怎样的拓扑特征？*本文对 20 个最常用的基准域进行了系统考察。我们的首个研究步骤是通过经验观察来审视示例实例的拓扑结构。我们选取了一组随机示例进行分析，这些示例的状态空间规模足够小，从而能够被完整构建。针对 FF 启发式函数的理想化版本（最优松弛距离，通常记为 h+），我们获得了以下三项关键发现：在 16 个域中，示例中不存在未识别的死角状态（即存在松弛规划但不存在实际规划的状态）；在 14 个域中，根本不存在局部最小值；在 8 个域中，最大退出距离（大致可理解为平坦区域上达到较优状态所需的最大步数）似乎存在一个恒定的上界。FF 实际采用的启发式函数（最优松弛距离的近似版本）在拓扑性质上表现出相似的特征。当具备上述三项属性时，FF 的搜索算法能够在找到目标之前对多项式数量的状态进行评估。

经验研究工作为我们揭示了规划领域之间的相关差异，下一步则是对总体观察结果进行验证。理论研究表明，针对最优松弛距离 h+，除了一个例外情况，我们所有小规模示例中观察到的现象实际上均可推广至相应的完整领域。通过这一验证过程，该研究进一步揭示了被调查领域中的常见*结构模式图*，正是这些结构特征赋予了松弛距离以较高的启发式质量，从而造就了 FF 等规划器优异的性能表现。这些结构性模式大致可归纳为：1. 可用的动作是可逆的或无需反转（→ 无死角）；2. 任何有利于解决实际任务的动作亦有利于解决对应的松弛任务（结合条件 1 → 无局部最小值）；3. 某些动作具有与应用上下文无关的删除效果，而其他动作最多需要连续执行常数次（结合条件 1 和 2 → 最大退出距离的恒定上界）。

最后一项经验研究步骤证实，最优松弛距离的启发式质量在很大程度上延续到了 FF 对这些距离的近似版本中。尤为值得注意的是，在所有前述三种结构模式同时出现的 20 个被调查领域中，有 8 个领域展现出 FF 的"大"多项式性能（尤其在物流领域中表现突出）。

前两项研究以会议论文形式发表。首次实证工作发表于 IJCAI'01：

规划基准中的本地搜索拓扑：一项实证分析，载于：*第17届国际人工智能联合会议论文集*，美国华盛顿，2001年8月。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.bib)）

理论分析论文发表于 AIPS'02：

规划基准中的本地搜索拓扑：理论分析，载于：*第六届国际人工智能规划与调度国际会议论文集*，2002年4月，法国图卢兹。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)）（[参考资料](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)[条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.bib)）

AIPS'02 论文的扩展与修订版本——涵盖 10 个新域（IPC-3 与 IPC-4 基准）的结果，以及对规划域之间主要差异的修订定义，其中纳入了针对 AIPS'02 中若干新成果的更新——发表于 JAIR：

J. Hoffmann，**《忽略删除列表的工作**[原理](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)**：规划基准中的本地搜索拓扑》**，*《人工智能研究》*，第24卷，2005年，第[685-758](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)页。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)）

JAIR 论文包含了概述性的证明草图。更长的技术报告（TR，138页）提供了研究的全部细节：

《忽略删除列表的工作[原理](http://fai.cs.uni-saarland.de/hoffmann/papers/ai03report.ps.gz)：规划基准中的本地搜索拓扑》，技术报告第185号，信息学院，2003年3月。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ai03report.ps.gz)）

***

**>>**TorchLight

这是我近期开发的一项工具。它允许**在不实际执行任何搜索的情况下分析搜索空间拓扑**。具体而言，TorchLight 能够完全自动地对 h+（参见上文）条件下的局部搜索拓扑做出结论，甚至无需开始生成任何搜索状态。其中的关键在于因果图与域转换图之间的拓扑及其属性之间的联系——这一思路在我完成上述工作数年后逐渐流行开来。简而言之，其基本性质如下：*若因果图是非循环的，且所有变量转换都是可逆的，则 h+ 条件下不存在局部最小值*。

这一基本结果可通过更局部的分析进行扩展，即关注因果图的某些子图而非完整结构，并允许某些不可逆转换的特殊情况。通过这些扩展，该准则还能够推导出 h+ 条件下退出距离的界限，并适用于 4 个标准基准域。尽管这只涵盖了基准域的一小部分，TorchLight 还提供了一种简单的采样方法：查看少量（默认值：10）随机生成的状态，对每个状态应用该准则，然后返回样本状态中该条件判定为"是"的比例。此"成功率"为任意规划任务的"难度"（更准确地说，是 h+ 的质量）提供了一种度量指标。

**TorchLight 的源代码已通过 GNU GPL 许可公开提供：[TorchLight.zip](http://fai.cs.uni-saarland.de/hoffmann/TorchLight.zip)**。

有关 TorchLight 的论文已发表于 JAIR'11 和 ICAPS'11（按以下顺序排列）：

J. Hoffmann，**在不运行任何搜索的情况下分析搜索拓扑：关于因果图与 h+ 之间的联系**，*《人工智能研究》*，第41卷，2011年，第155-229页。（[PDF文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair11.pdf)）

J. Hoffmann，**《忽略删除列表的工作***原理***，第二部分：因果图》**，载于第21届国际自动规划与调度会议（ICAPS'11），2011年6月，德国弗赖堡。获最佳论文奖提名。（[pdf档案](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11.pdf)）

此外，还可参阅易于理解的 [ICAPS'11 演示文件（含示例运行）](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11-demo.pdf)、笔者的[演讲幻灯片](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11-slides.pdf)或 [ICAPS'11 演示海报](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11-poster.pdf)。


--------------------



**>>FF常规信息**

Fast-Forward（缩写为 FF）是由 Joerg Hoffmann 开发的与领域无关的规划系统。FF 能够处理经典的 STRIPS 以及全面的 ADL 规划任务，这些任务以 PDDL 格式进行描述（关于可处理数值状态变量的版本，请参见[另一页面](http://fai.cs.uni-saarland.de/hoffmann/metric-ff.html)）。该系统采用 C 语言实现，已参加[第二届国际规划竞赛](http://www.cs.toronto.edu/aips2000)的全自动赛道。竞赛结果中，FF 被授予"A 组杰出性能规划系统"称号，并荣获 Miconic 10 电梯领域 ADL 赛道最佳性能规划系统的迅达奖。该系统（经轻微调试后）还参加了[第三届国际规划竞赛](http://www.dur.ac.uk/d.p.long/competition.html)，在 STRIPS 领域中表现出色（但由于其他竞争系统具有更广泛的语言覆盖范围，未获得奖项）。请查阅我们的[网页](http://fai.cs.uni-saarland.de/hoffmann/2002.html)，其中提供了竞赛中使用的 STRIPS（及数值）域运行时数据和求解长度数据的 gnuplot 图表。在当前页面中，我们提供了第三届国际规划竞赛中使用的源代码，以及一些较旧版本的源代码，以便 STRIPS 版本更易于阅读。我们还提供了与该系统相关的出版物索引，以及阐述该系统在众多基准域中高效运行原理的有趣信息。

**>>基本原理**

FF 是一种前向启发式状态空间规划器。其主要的启发式原理最初由 [Blai Bonet](http://www.cs.ucla.edu/~bonet/) 和 [Hector Geffner](http://www.ldc.usb.ve/~hector/) 针对 HSP 系统提出：为了获得启发式估计，通过忽略所有运算符的删除列表，将当前任务 **P** 松弛为更简单的任务 **P+**。HSP 采用了一种技术来给出 **P+** 求解长度的粗略估计，而 FF 则通过图规划式的算法，显式地提取出 **P+** 的显式解。松弛解中的动作数被用作目标距离的估计值。这些估计值控制着一种新颖的局部搜索策略——*强制爬山（Enforced Hill Climbing）*：这是一个爬山过程，在每个中间状态下，使用广度优先搜索来找到*严格更优的*、可能是间接的后继状态。作为第二项重要的启发式信息，松弛规划可用于修剪搜索空间：通常，在一个状态中真正有用的动作包含在松弛规划中，因此可以将任何状态的后继状态限定为各自松弛解中的成员。FF 采用了这种启发式的略加精细的形式，我们称之为*有用动作修剪（Helpful Actions Pruning）*。上述简单架构已能高效地解决大多数可用的基准测试问题。存在问题的情形是 *死胡同（Dead Ends）*——即无法到达目标的状态——或 *目标排序（Goal Ordering）*问题。在后一种现象存在的情况下（例如在 Blocksworld 中），局部搜索有时会过于贪婪地进行而被困住。为克服这一问题，我们基于松弛解集成了目标议程算法（由 [Jana Koehler](http://www.informatik.uni-freiburg.de/~koehler) 首次提出），以及我们自有的简单目标排序技术。为处理可能导致搜索彻底失败的死角状态，我们选择了一个简单的安全网方案：若局部搜索失败，则忽略此前进行的所有操作，切换到完整的"最佳优先"算法，仅按目标距离评估值的顺序扩展*所有*搜索节点。

**>>源代码可用**

FF 依据 GNU 通用公共许可证（GPL）公开提供。关于 Metric-FF 的源代码，请参见[其他网页](http://fai.cs.uni-saarland.de/hoffmann/metric-ff.html)。FF-v2.3 位于[此处](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3.tgz)。此为 ADL 版本，通过我们自有的目标排序修剪技术以及摘录自 [Jana Koehler](http://www.zurich.ibm.com/~koe/) 著作的"目标议程"提供的排序信息进行了增强。该版本与第二届国际规划竞赛中使用的 FF-v2.2 版本相同，仅对预处理阶段中的一些小错误进行了移除。

那些曾与 FF 源代码打交道的人可能已经注意到，解析器多年来一直存在兼容性问题——该解析器编写于 1997 年，已不再兼容最新的 bison/flex 版本。在此，我要**向斯特拉斯克莱德大学的 Andrew Coles 表示衷心的感谢，他花费了大量时间研究并解决了这一问题。** [上述链接](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3.tgz)提供了 FF-v2.3 的新修补版本。Andrew 已使用 flex 2.5.34 和 2.5.35 以及 bison 2.3 和 2.4.1 对其进行了测试。最终发现所需的更改相当简洁。以下是 Andrew 的描述：

-   在 lex-fct_pddl.l 中，将 "#define fct_pddlwrap() 1" 替换为 "int fct_pddlwrap() {return 1;};"
-   在 lex-ops_pddl.l 中，将 "#define ops_pddlwrap() 1" 替换为 "int ops_pddlwrap() {return 1;};"

Robert Goldman 友善地贡献了 [FF-v2.3 的一个补丁版本](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3-newlines-parse-goldman.tgz)，[该版本中的解析器允许在类型列表中使用换行符](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3-newlines-parse-goldman.tgz)。

最后，Martin Suda 提供了 [FF-v2.3 的一个修补版本](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3-big-parse-suda.tgz)，该版本中的解析器应能够解析较大的输入。笔者尚未对其进行测试，但仍希望能为您提供这一版本。

**>>相关论文**

-   比赛中使用的 FF 系统的详细 JAIR 文章（FF-v2.2/3）。
    
    [B. Nebel](http://www.informatik.uni-freiburg.de/~nebel)， **《FF 规划系统：通过启发式搜索快速生成规划》**，载于：《人工智能研究杂志》，第14卷，2001年，第[253-302](http://fai.cs.uni-saarland.de/hoffmann/papers/jair01.ps.gz)页。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/jair01.bib)）
    
-   一篇简短且易于阅读的论文，总结了上述文章的诸多内容，发表于 AI 杂志。
    
    FF：快进规划系统，载于：AI 杂志，第22卷，第3期，2001年，第[57-62](http://fai.cs.uni-saarland.de/hoffmann/papers/aimag01.ps.gz)页。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/aimag01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aimag01.bib)）
    
-   我们进行了一项大规模的实证研究，确定了 HSP 与 FF 之间的关键差异。我们的研究发现构成了上述 JAIR 文章的一部分，并在 IJCAI'01 关于 AI 经验方法的研讨会上进行了介绍。
    
    [B. Nebel](http://www.informatik.uni-freiburg.de/~nebel)， **《什么使 HSP 和 FF 有所不同？》**，载于 IJCAI'01 AI 经验方法研讨会，2001年8月，美国华盛顿州西雅图市。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01-ws.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01-ws.bib)）
    
-   我们研究了规划基准的结构属性，深入阐明了 FF 及其他先进的启发式搜索规划器成功的原因。相关论文发表于 IJCAI'01、AIPS'02 和 JAIR。JAIR 文章为最新版本，在各方面均值得强烈推荐。
    
    规划基准中的本地搜索拓扑：一项实证分析，载于：*第17届国际人工智能联合会议论文集*，美国华盛顿，2001年8月。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.bib)）
    
    规划基准中的本地搜索拓扑：理论分析，载于：*第六届国际人工智能规划与调度国际会议论文集*，2002年4月，法国图卢兹。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)）（[参考资料](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)[条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.bib)）
    
    J. Hoffmann，**《忽略删除列表的工作**[原理](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)**：规划基准中的本地搜索拓扑》**，*《人工智能研究》*，第24卷，2005年，第[685-758](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)页。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)）
    
-   在 ISMIS'00（2000年10月11日至14日，北卡罗来纳州夏洛特）上发布了关于 FF 首个 STRIPS 版本（FF-v1.0）的简短论文，并在 ECAI 2000 研讨会 PuK2000（2000年8月20日至25日，柏林）上发表了关于该论文新成果的报告。
    
    载于：2000年10月在美国北卡罗来纳州夏洛特*举行的第12届国际智能系统方法论国际会议论文集。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ismis00.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ismis00.bib)）
    
-   针对 FF 修改的"目标议程"机制论文。[Jana Koehler](http://www.informatik.uni-freiburg.de/~koehler) 的原始论文发表于 AIPS-98 会议。与 Joerg Hoffmann 合作撰写了一篇更详细的文章，正式介绍了该方法，发表于 JAIR。
    
    [J. Koehler](http://www.informatik.uni-freiburg.de/~koehler)， **《通过提取子问题解决复杂规划任务》**，载于：*第4届人工智能规划与调度会议论文集*，美国宾夕法尼亚州匹兹堡，1998年7月。（[gzip后记文件](http://www.informatik.uni-freiburg.de/~koehler/papiere/aips-98.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aips-98.bib)）
    
    [J. Koehler](http://www.informatik.uni-freiburg.de/~koehler)， 载于：人工智能研究杂志，2000年第12卷，第[338-386](http://fai.cs.uni-saarland.de/hoffmann/papers/jair00.ps.gz)页（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair00.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/jair00.bib)）
    
-   最后，有一些工作描述了 IPP 用于利用领域定义的结构属性将完整的 ADL 任务编译为命题范式的预处理方法。在 FF 中，该方法已通过一种可达性分析阶段进行了扩展和更高效的实现。描述 IPP 预处理方法的论文曾在 ECAI 2000 研讨会上进行介绍。
    
    [J. Koehler](http://www.informatik.uni-freiburg.de/~koehler) 与 J. Hoffmann， **《关于涉及任意一阶公式的 ADL 运算符的实例化》**，将发表于 ECAI 2000 规划、调度与设计新结果研讨会（PuK2000），2000年8月，德国柏林。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ecai00-ws.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ecai00-ws.bib)）



***







