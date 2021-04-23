[TOC]

https://github.com/pucrs-automated-planning/pddl-parser Classical Planning in Python

- [PDDL.py](https://github.com/pucrs-automated-planning/pddl-parser/blob/master/PDDL.py)用PDDL解析器
- 有计划者的[planner.py](https://github.com/pucrs-automated-planning/pddl-parser/blob/master/planner.py)

# ffPlaner

在线编辑求解FF Planer online： http://editor.planning.domains/#      

注意不要使用https，否则会报malformed url

http://www.ai.mit.edu/courses/16.412J/ff.html  大学教程链接有一个tireworl轮胎更换域实例：

> ff -o tyreworld_domain.pddl -f tyreworld_facts1


https://fai.cs.uni-saarland.de/hoffmann/ff.html ff官方下载主页

 FF规划器是智能规划界最富盛名的作品，采用经典的前向搜索方法，结合启发式算法有效提高了规划算法搜索效率，在多次世界规划大赛中都有好的名次。

下载镜像 http://www.pudn.com/Download/item/id/2027550.html

使用：在ff文件同目录下运行


```
./ff -o ./ff-domains/domain.pddl -f ./ff-domains/data.pddl
```


也可以将ff复制到/etc/bin下，命令为```sudo cp ff /etc/bin```，运行ff时只需在命令行中输入

```
ff -o ./ff-domains/domain.pddl -f ./ff-domains/data.pddl
```


demo


这里还有很多例子：

http://fai.cs.uni-saarland.de/hoffmann/ff-domains.html 该页面是由Joerg Hoffmann创建的，它是想要在规划中进行大规模实证研究的人们的起点。FF域集合为20个STRIPS和ADL规划基准域提供（可能的话）生成器，包括两个竞赛中使用的示例。下面，我们为每个域提供有关起源，进行的调整（如果有），生成器的参数以及随机化策略的信息。可以下载域文件和生成器的C源代码。单击[此处](http://fai.cs.uni-saarland.de/hoffmann/ff-domains.tgz) 下载整个软件包。关于如何生成它们（包括makefile）以及如何运行它们，生成器应该是不言自明的。在不太明显的情况下，我们还包括了README文件。

Ubuntu系统运行FF-planner 


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

安装bison即可

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
   ;给出依赖项，比如这里的三个都是依赖项，语法使用是“:依赖项”,
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
   ；谓词名称最先给出，然后依次给出该谓词的项，格式为“？参数 – 参数类型”，
   ；比如这里的“？x – physob ？y – physob”表示x这个参数的类型应该是physob的，不能传递其他类型的参数。
   ；整个“Tire ？x – physob”对应Tire(x)这一原子（公式）。
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

- breiefcase world

forall和when的用法,首先讲一下这个domain的含义，然后将下面的forall和when用法

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

然后就是数据文件，给出这个问题的定义：

它涉及的domain、
问题的参数定义、
问题的初始状态、
问题的目标状态

定义好问题后我们调用求解器，他会给我们求解出一系列的action使得问题从初始状态到达目标状态（如果有解）


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
        ; todo:   put  the   initial   state ’ s   facts  and  numeric  values  here
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

:•clear(x): there is no block on top of block x;

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
        ; todo :put  the   initial   state ’ s   facts  and  numeric  values   here
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

FF规划器并不能生成最优的方案，例如在Puzzle问题中就出现了连续拨动数字6的情况，经过手动验证两个问题的Plan都是正确的。（注：代码中的注释由Vscode插件自动生成）

--------------------------------------------------------------------------------------------------------------------------

**>>规划基准中的本地搜索拓扑**

FF的性能带来的最令人振奋的问题之一是，*为什么*在这么多领域如此有效？启发式算法（尤其是局部搜索算法）的成功取决于其使用的启发式函数的质量，即取决于使用该启发式函数进行评估的基础搜索空间的*局部搜索拓扑*，这是有争议的。所以问题归结为，*在FF运作良好的那些域中，搜索空间的特征拓扑特性是什么？*我们调查了20个最常用的基准域。我们的第一个研究工作是凭经验观察示例实例的拓扑。我们查看了一些随机示例的集合，这些示例的状态空间小到可以完全构建。对于FF启发式函数的理想版本（最佳松弛距离，通常表示为h +），我们进行了以下三个关键观察：在示例中没有未识别的死角状态（存在松弛规划但没有实际规划的状态）在16个域中；在14个域中根本没有本地最小值；在8个域中，最大出口距离（大致是平坦区域上达到较好状态的最大距离）似乎有一个恒定的上限。FF'的拓扑性质 的实际启发式函数（最佳松弛距离的近似值）相似。具有这三个属性，FF的搜索算法会在找到目标之前对多项状态进行多项式评估。

经验工作为我们提供了规划领域之间的相关区别，下一步是验证总体观察结果。理论研究证明，对于最佳松弛距离h +，除了一个例外，我们所有小示例中的所有观察结果实际上都延续到相应的整个域。通过验证过程，调查还提供了常见*的结构模式图*在被调查的领域中，这些问题会导致放松距离的高启发式质量，从而导致FF等计划者的表现。结构的模式非常粗糙：1.可用的动作是可逆的或不需要反转（->无死角）；2.任何有利于解决实际任务的动作也有利于解决轻松的任务（与1.->没有局部最小值）一起；3.有些动作具有与应用无关的删除效果，而其他动作最多需要连续执行恒定的次数（以及1.和2。->最大退出距离的恒定上限） 。

最后的经验工作步骤证实，最佳松弛距离的启发式质量在很大程度上延续了FF对这些距离的近似。尤其是，在所有上述三种结构模式均出现的被调查的20个域中的八个域中，FF是“大”多项式（尤其是在物流域中）。

前两个调查作为会议论文发表。首次实证工作在IJCAI'01上发表：

规划基准中的本地搜索拓扑：一项实证分析，载于：*第17届国际人工智能联合会议论文集*，美国华盛顿，2001年8月。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.bib)）

关于理论分析的论文发表在AIPS'02上：

规划基准中的本地搜索拓扑：理论分析，载于：2002年4月在法国图卢兹*举行的第六届国际人工智能规划与调度国际会议论文集上*。（[gzip的后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)）（[参考资料](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)[条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.bib)）

AIPS'02文件的扩展和修订版，包括10个新域的结果（IPC-3和IPC-4基准），以及对规划域之间主要区别的修订定义，其中涉及针对AIPS'02的几个新结果JAIR中发布了20个``旧''域：

J. Hoffmann，**《忽略删除列表的工作**[原理](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)**：规划基准中的本地搜索拓扑》**，*《人工智能研究》*，第24卷，2005年，第[685-758](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)页。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)）

JAIR论文包含概述证明草图。较长的TR（138页）提供了调查的全部详细信息：

忽略删除列表的工作[原理](http://fai.cs.uni-saarland.de/hoffmann/papers/ai03report.ps.gz)：《规划基准中的本地搜索拓扑》，技术报告第185号，信息学院，2003年3月。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ai03report.ps.gz)）

***

**>>**TorchLight

这是我最近开发的工具。它允许**分析搜索空间拓扑，而无需实际运行任何搜索**。我的意思是，TorchLight可以完全自动地在h +（参见上文）下对本地搜索拓扑得出结论，甚至无需开始生成任何搜索状态。关键是因果图和域转换图的拓扑和属性之间的联系，正如我在完成上述工作后几年流行起来的那样。简而言之，基本属性是：*如果因果图是非循环的，并且所有变量转换都是可逆的，则h +下没有局部最小值*。

基本结果可以通过更局部的分析来扩展，着眼于因果图的某些子图而不是完整的子图，并允许某些不可逆转换的特殊情况。通过这些扩展，该标准还允许导出h +下出口距离的界限，并且适用于4个标准基准域。虽然这只是基准的一小部分，但TorchLight还具有一种简单的采样方法，可以查看少量（默认值：10）随机生成的状态，将每个状态的准则应用到每个状态，然后返回样本状态中条件说“是”。此“成功率”提供了针对任意计划任务的“硬度”（更准确地说，是h +的质量）的度量。

**TorchLight的源代码已通过GNU GPL许可公开提供：[TorchLight.zip](http://fai.cs.uni-saarland.de/hoffmann/TorchLight.zip)**。

有关TorchLight的论文已在JAIR'11和ICAPS'11上发表（按以下顺序排列：-）

J. Hoffmann，在**不运行任何搜索的情况下分析搜索拓扑：关于因果图与h +之间的联系**，*《人工智能研究》*，第41卷，2011年，第155-229页。（[PDF文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair11.pdf)）

J. Hoffmann，**“忽略删除列表的工作***原理***，第二部分：因果图”**，在2011年6月于德国弗赖堡*举行的第21届国际自动规划和计划会议（ICAPS'11）上发表*。被提名最佳论文奖。 （[pdf档案](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11.pdf)）

还有一个易于阅读的[ICAPS'11演示文件，其中包含示例运行](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11-demo.pdf)，您可以查看我的[演讲幻灯片](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11-slides.pdf)或[ICAPS'11演示海报](http://fai.cs.uni-saarland.de/hoffmann/papers/icaps11-poster.pdf)。


--------------------



**>>FF常规信息**

Fast-Forward，缩写为FF，是Joerg开发的与领域无关的计划系统。FF可以处理经典的STRIPS-以及全面的ADL-计划任务，这些任务将在PDDL中指定（对于可以处理数字状态变量的版本，请查看[另一页](http://fai.cs.uni-saarland.de/hoffmann/metric-ff.html)）。该系统在C语言中实现。它已经参加了[第二届国际计划竞赛的](http://www.cs.toronto.edu/aips2000)全自动赛道。比赛的结果是，FF被授予``A组杰出绩效计划系统''，并且还获得了Miconic 10电梯领域ADL轨道上表现最佳的计划系统的迅达奖。该系统（略有调试）还参加了[第三届国际计划竞赛](http://www.dur.ac.uk/d.p.long/competition.html)在STRIPS领域表现出色（但由于其他竞争系统的语言覆盖面更广，因此没有获得奖项）。请查看我们的[网页，在竞赛中使用的STRIPS（和数字）域中提供运行时数据和解决方案长度数据的gnuplot](http://fai.cs.uni-saarland.de/hoffmann/2002.html)。在当前页面上，我们提供了第三届国际计划竞赛中使用的源代码，以及一些较旧的源代码，以使STRIPS版本更易读。我们还提供了与该系统相关的出版物的指针，并提供了一些有趣的信息，说明了使该系统在许多基准域中如此高效的原因。

**>>基本原理**

FF是前向启发式状态空间规划师。主要的启发式原理最初是由[Blai Bonet](http://www.cs.ucla.edu/~bonet/)和[Hector Geffner](http://www.ldc.usb.ve/~hector/)针对HSP系统开发的：要获得启发式估计，通过忽略所有运算符的删除列表，将手头的任务**P** *放松*为更简单的任务**P +**。而HSP采用了一种技术，给出了的溶液长度的粗略估计**P +**，FF *提取的显式解*到**P +**，通过使用图规划式算法。松弛解中的动作数用作目标距离估计。这些估算值控制着一种新颖的本地搜索策略，*强制爬山*：这是一个爬山程序，在每个中间状态下，都使用广度优先搜索来找到*严格更好的*，可能是间接的后继程序。作为第二个重要的启发式信息，放松的计划可用于修剪搜索空间：通常，在一个状态中真正有用的动作包含在放松的计划中，因此可以将任何状态的后继者限制为成员各自放松的解决方案。FF运用了这种启发式的稍微详细的形式，我们称其为*有用的动作修剪*。到目前为止描述的简单体系结构已经非常有效地解决了大多数可用的基准测试。有问题的情况是 *死胡同*---无法达到目标的状态---或*目标排序*。在后一种现象的存在下，例如在Blocksworld中，本地搜索有时会过于贪婪地进行，并被困住。为了克服这个问题，我们基于轻松的解决方案集成了目标议程算法（由[Jana Koehler](http://www.informatik.uni-freiburg.de/~koehler)首次提出），以及我们自己的简单目标排序技术。为了处理可能导致搜索完全失败的死角状态，我们选择了一个简单的安全网解决方案：如果本地搜索失败，那么我们将跳过目前为止所做的所有事情，并切换到完整的“最佳优先”算法，只需增加目标距离评估的顺序即可扩展*所有*搜索节点。

**>>源代码可用**

FF是根据GNU通用公共许可证公开提供的。有关Metric-FF的源代码，请参见[其他网页](http://fai.cs.uni-saarland.de/hoffmann/metric-ff.html)。FF-v2.3在[这里](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3.tgz)。这是ADL版本，通过我们自己的目标排序修剪技术以及“目标议程”提供的排序信息进行了增强，该信息摘自[Jana Koehler](http://www.zurich.ibm.com/~koe/)的著作。它与第二届国际规划大赛中使用的FF-v2.2版本相同，对预处理阶段中的一些小错误进行了模删除。

那些曾经与FF联系过的人可能会意识到，解析器多年来一直存在麻烦，该解析器编写于1997年，不再符合最新的bison / flex版本。我要**对斯特拉斯克莱德大学的安德鲁·科尔斯（Andrew Coles）表示衷心的感谢，他花了一些时间研究并解决这个问题。** [上面的链接](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3.tgz)提供了FF-v2.3的新修补版本。安德鲁已使用flex 2.5.34和2.5.35以及野牛2.3和2.4.1对它进行了测试。毕竟，所需的更改非常简单。这是安德鲁的描述：

-   在lex-fct\_pddl.l中，将“ #define fct\_pddlwrap（）1”替换为“ int fct_pddlwrap（）{return 1;};”
-   在lex-ops\_pddl.l中，将“ #define ops\_pddlwrap（）1”替换为“ int ops_pddlwrap（）{return 1;};”

罗伯特·戈德曼（Robert Goldman）友善地贡献了[FF-v2.3](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3-newlines-parse-goldman.tgz)的[补丁版本，其中解析器允许在类型列表中使用换行符](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3-newlines-parse-goldman.tgz)。

最后，马丁·苏达（Martin Suda）提供了[FF-v2.3的修补版本，该解析器应该能够解析较大的输入](http://fai.cs.uni-saarland.de/hoffmann/ff/FF-v2.3-big-parse-suda.tgz)。我还没有测试过，但还是想让你拥有它。

**>>相关论文**

-   在比赛中使用了有关FF系统的详细JAIR文章（FF-v2.2 / 3）。
    
    [B. Nebel](http://www.informatik.uni-freiburg.de/~nebel)， **《 FF计划系统：通过启发式搜索快速生成计划》**，发表于：人工智能研究杂志，第14卷，2001年，第[ 253-302](http://fai.cs.uni-saarland.de/hoffmann/papers/jair01.ps.gz)页。（[gzip的附言文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/jair01.bib)）
    
-   简短的易于阅读的论文总结了以上文章的许多内容，并在AI杂志上发表。
    
    FF：快进计划系统，在：AI杂志，第22卷，第3期，2001年，第[57-62 ](http://fai.cs.uni-saarland.de/hoffmann/papers/aimag01.ps.gz)页。（[gzip的附言文件](http://fai.cs.uni-saarland.de/hoffmann/papers/aimag01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aimag01.bib)）
    
-   我们进行了大规模的实证研究，确定了HSP和FF之间的关键差异。我们的发现的描述构成了上面JAIR文章的一部分，并已在IJCAI'01关于AI的经验方法的研讨会上进行了介绍。
    
    [B. Nebel](http://www.informatik.uni-freiburg.de/~nebel)， **什么使HSP和FF有所不同？**，在2001年8月在美国华盛顿州西雅图市*IJCAI'01的AI经验方法研讨会上*进行了介绍。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01-ws.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01-ws.bib)）
    
-   我们研究了计划基准的结构属性，阐明了FF和其他先进的启发式搜索计划程序成功的原因。论文在IJCAI'01，AIPS'02和JAIR上发表。JAIR文章是最新的，并且在所有方面都绝对值得推荐。
    
    规划基准中的本地搜索拓扑：一项实证分析，载于：*第17届国际人工智能联合会议论文集*，美国华盛顿，2001年8月。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ijcai01.bib)）
    
    规划基准中的本地搜索拓扑：理论分析，载于：2002年4月在法国图卢兹*举行的第六届国际人工智能规划与调度国际会议论文集上*。（[gzip的后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)）（[参考资料](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.ps.gz)[条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aips02.bib)）
    
    J. Hoffmann，**《忽略删除列表的工作**[原理](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)**：规划基准中的本地搜索拓扑》**，*《人工智能研究》*，第24卷，2005年，第[685-758](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)页。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair05b.ps.gz)）
    
-   在ISMIS'00（2000年10月11日至14日，北卡罗莱纳州夏洛特）上发布了有关FF的首个STRIPS版本的简短论文（FF-v1.0），并在ECAI 2000研讨会PuK2000上发表了一篇有关该论文新成果的论文。规划，进度安排和设计（柏林，2000年8月20日至25日）。
    
    ，见： 2000年10月在美国北卡罗来纳州夏洛特*举行的第12届国际智能系统方法论国际会议论文集*。（[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ismis00.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ismis00.bib)）
    
-   关于“目标议程”机制的论文已经针对FF进行了修改。[Jana Koehler](http://www.informatik.uni-freiburg.de/~koehler)的原始论文在AIPS-98会议上。与Joerg Hoffmann合作撰写了一篇更详细的文章，正式介绍了该方法，并在JAIR上发表。
    
    [J. Koehler](http://www.informatik.uni-freiburg.de/~koehler)，“ **通过提取子问题解决复杂的计划任务”** ，载于： *第4届人工智能计划与调度会议论文集*，美国宾夕法尼亚州匹兹堡，1998年7月。（[gzip后记文件](http://www.informatik.uni-freiburg.de/~koehler/papiere/aips-98.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/aips-98.bib)）
    
    [J. Koehler](http://www.informatik.uni-freiburg.de/~koehler)，， 于：人工智能研究杂志，2000年第12卷，第[338-386 ](http://fai.cs.uni-saarland.de/hoffmann/papers/jair00.ps.gz)页（用[gzip压缩的后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/jair00.ps.gz)）（[围嘴条目](http://fai.cs.uni-saarland.de/hoffmann/papers/jair00.bib)）
    
-   最后，有一些工作描述了IPP用于利用领域定义的结构属性将完整的ADL任务编译为命题范式的预处理方法。对于FF，此方法已更有效地实施，并通过一种可达性分析阶段进行了扩展。在ECAI 2000研讨会上介绍了描述IPP预处理方法的论文。
    
    [J. Koehler](http://www.informatik.uni-freiburg.de/~koehler)和J.Hoffmann， **关于涉及任意一阶公式的ADL运算符的实例化**，将 *在2000年* 8月于德国柏林*ECAI 2000举行的规划，日程安排和设计新结果研讨会（PuK2000）上发表*。 （[gzip后记文件](http://fai.cs.uni-saarland.de/hoffmann/papers/ecai00-ws.ps.gz)）（[围兜条目](http://fai.cs.uni-saarland.de/hoffmann/papers/ecai00-ws.bib)）
    

***




