# 求解器综述

## IPC 赛事：问题起源与发展脉络

https://www.icaps-conference.org/competitions/  该链接汇总了历届比赛的完整信息


An Overview of the International Planning Competition   chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://www.nms.kcl.ac.uk/andrew.coles/PlanningCompetitionAAAISlides.pdf


https://helios.hud.ac.uk/scommv/IPC-14/selection.html 2014年


International Planning Competition

https://ipc2018-classical.bitbucket.io/ 2018年


eecs.oregonstate.edu/ipc-learn/ 第六届

cs.cmu.edu/afs/cs/project/jair/pub/volume20/long03a-html/node2.html
  国际规划大赛系列



依据问题特性，主要可划分为如下两类：

经典规划（Classical Planning, CP）：每个实例对应于一个独立的解；

通用规划（General Planning, GP）：多个实例共享同一个解子图算法（即控制流图 Control Flow Graph），常见形式化范式包括 QNP 与 FOND。

## CP：经典规划

FF

FD

LAPKT

## GP：通用规划



- MyND

- PRP

- FOND-SAT

- PRP_planner-for-relevant-policies



从宏观视角审视，学界通常沿两条技术路径展开探索：

自顶向下（Top-Down）方法：在与或树（亦可理解为控制流图 Control Flow Graph）中进行搜索，从而得到类算法（algorithm-like）的策略（policy）。就其本质而言，这乃是符号化 goto 语句所对应的底层汇编算法的等价表述。

以及

自底向上（Bottom-Up）方法：在经典规划中生成实例，据此完善并补全抽象图，并以响应式方式持续打补丁。FOND-SAT 可被视为一种文法自动机，通过符号 SAT 可满足性求解实现规划。据本文作者理解，其本质归属于自顶向下（Top-Down）的"求解"范式。

诸如 Merging Example Plans into Generalized Plans for Non-deterministic Environments 以及 Directed Search for Generalized Plans Using Classical Planners 等研究工作即属于此类范畴。

> 正如 Dijkstra 在其经典著作中所阐述的，编程应当是经由严谨思考与推理所得的算法产物，而不应是在意大利面条式代码中盲目调试、反复试错，以及为各种特殊情况仓促打补丁的结果。
>
> 图灵所开创的自动编程篇章，令人坚信规划（plan）将是一种优雅的解法。

QNP 的提出，实际上是受模拟包含 while 循环的链表反转（Linked List Reverse）过程的启发。此类问题的解子图策略（policy），本质上便是**包含 while 循环的算法（algorithm）**。

从实例中学习时，不可避免地需要考量**覆盖率**（即已解决问题数目占规划问题总数的比例）。我们设想，倘若存在一个较为完善的通用规划（GP）的良性定义，其结果应当是经过精心设计的自顶向下结构的产物，而非仓促上线、不断打补丁的拼合体——尽管在多数实践场景中，后者往往成为常态。

一个较为合适的算法示例是三数之和问题：

> 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c，使得 a + b + c = 0？请找出所有满足和为 0 且不重复的三元组。
>
> 注意：答案中不得包含重复的三元组。
>

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        for(int i =0;i<nums.size();i++){
            if(nums[i] > 0) return res;
            // 错误去重方法，将会漏掉-1,-1,2 这种情况
            /*
            if (nums[i] == nums[i + 1]) {
                continue;
            }
            */
            // 正确去重方法
            if(i >0 && nums[i] == nums[i - 1] ){
                continue;
            };
            int left = i+1;
            int right = nums.size() -1;
            while(left < right){
                // 去重复逻辑如果放在这里，0，0，0 的情况，可能直接导致 right<=left 了，从而漏掉了 0,0,0 这种三元组
                /*
                while (right > left && nums[right] == nums[right - 1]) right--;
                while (right > left && nums[left] == nums[left + 1]) left++;
                */
                if(nums[i] + nums[left] + nums[right] > 0){
                    right --;
                }else if(nums[i] + nums[left] + nums[right] <  0){
                    left++;
                }else{//nums[i] + nums[left] + nums[right] = 0
                    res.push_back(vector<int>{nums[i], nums[left], nums[right]});
                    // 去重逻辑应该放在找到一个三元组之后
                    while (right > left && nums[right] == nums[right - 1]) right--;
                    while (right > left && nums[left] == nums[left + 1]) left++;

                    // 找到答案时，双指针同时收缩
                    right--;
                    left++;
                }    
            }
        }
        return res;
    }
};
```

审视上述示例，需着重关注以下要点：

> 错误的去重方法将会遗漏诸如 -1, -1, 2 这类情形；去重逻辑的放置位置亦会对最终结果产生显著影响，例如 0, 0, 0 的案例所示。

由此可得出的启示，正如 Dijkstra 在其著作中所阐述的：唯有自顶向下（Top-Down）的精巧设计，方能产生兼具实用价值与强鲁棒性的算法解，而非仅止于玩具级别的实现。

而这一点，恰恰是从实例经典规划（CP）中学习通用规划（GP）抽象图、不断打补丁的自底向上（Bottom-Up）方法所无法习得的。经由后者所习得的 GP 抽象控制流图往往千疮百孔、遍布补丁，甚至无法通过足够的测试用例以满足所需的测例覆盖率。

## 为何 CFG 控制流图是最佳中间表示（Intermediate Representation, IR）方法

## Planning Graph Analysis：规划图分析

Fast planning through planning graph analysis 1997

https://dblp.uni-trier.de/pid/b/AvrimBlum.html 作者主页

2003 SAT-Based Model-Checking of Security Protocols Using Planning Graph Analysis.

2006

2017

link.springer.com/chapter/10.1007%2F3-540-46238-4_31

On Plan Adaptation through Planning Graph Analysis

A Planning Heuristic Based on Causal Graph Analysis 2004

aaai.org/Library/ICAPS/2004/icaps04-021.php

上述问题对于基于规划图（如 IPP、Graphplan 和 Blackbox）的现行规划器而言，具有重要的理论意义与实践价值。

## 面向动态图的最新路径查找算法

面向动态图（D*、D* Lite、LPA* 等）的最新路径查找算法之间存在何种本质差异？

https://qastack.cn/cstheory/11855/how-do-the-state-of-the-art-pathfinding-algorithms-for-changing-graphs-d-d-l

截至目前所整理的相关算法清单如下：

\```

D*（1994年）

Focused D*（1995年）

Dynamic SWSF-FP（1996年）

LPA（1997年）

LPA* / Incremental A*（2001年）

D* Lite（2002年）

SetA*（2002年）

HPA*（2004年）

Anytime D*（2005年）

PRA*（2005年）

Field D*（2007年）

Theta*（2007年）

HAA*（2008年）

GAA*（2008年）

LEARCH（2009年）

BDDD*（2009年——笔者无法获取该论文）

Incremental Phi*（2009年）

GFRA*（2010年）

MTD*-Lite（2010年）

Tree-AA*（2011年）

\```

可以在上述问题栏中找到每篇论文的对应链接。

简单重计算

\```

D*（亦称 Dynamic A*，1994年）：在初次运行时，D* 的行为与 A* 高度相似，能够迅速找到从起点至终点的最优路径。然而，当单元沿路径移动且图结构发生变化时，D* 能够极为高效地重新计算从当前单元位置至终点的最优路径，其速度远超重新运行 A* 的方案。然而，D* 以其实现复杂性而著称，更为简洁的 D* Lite 已完全取代了 D*。

Focused D*（1995年）：对 D* 的改进，旨在提升运算速度以实现"更接近实时"的性能表现。笔者未能找到其与 D* Lite 的直接对比资料，但鉴于其提出年代较早且 D* Lite 的讨论更为广泛，可以合理推断 D* Lite 更具优势。

Dynamic SWSF-FP（1996年）：存储从每个节点至目标节点的距离估算值。初始设置阶段需计算所有距离，计算开销较大。当图结构发生变化后，该算法仅更新距离发生变化的节点。该算法与 A* 及 D* 无直接关联。适用于每次变更后需计算从多个节点至目标距离的场景；否则，LPA* 或 D* Lite 通常是更为实用的选择。

LPA* / Incremental A*（2001年）：LPA*（Lifelong Planning A*，亦称 Incremental A*，有时被混淆地简称为"LPA"，但其与另一同名算法并无关联）是 Dynamic SWSF-FP 与 A* 的结合体。初次运行时，其行为与 A* 完全一致。然而，在图结构发生小幅变更后，相比于重新运行 A* 进行同一起讫点对的搜索，LPA* 能够利用先前运行中积累的信息，大幅减少需要检查的节点数量。这恰好契合了笔者的需求，因此 LPA* 被认为是最佳选择。LPA* 与 D* 的不同之处在于，它始终寻求从同一固定起点到同一固定终点的最优路径，不适用于起点发生移动的场景（例如沿初始最优路径移动的单元）。然而……

D* Lite（2002年）：该算法利用 LPA* 来模拟 D* 的行为。换言之，当单元沿初始最优路径移动且图结构发生变化时，D* Lite 调用 LPA* 来计算该单元的新最优路径。D* Lite 被公认在实现上远比 D* 简洁，并且其运行速度始终不逊于 D*，因此已完全淘汰了 D*。从任何角度来看，都没有继续使用 D* 的充分理由，建议改用 D* Lite。

任意角度运动

Field D*（2007年）：D* Lite 的一种变体，不再将运动限制于网格约束之内。换言之，最优路径可使单元沿任意角度移动，而不仅限于网格点之间的 45 度（或 90 度）方向。该技术已被美国国家航空航天局（NASA）应用于火星探测车的路径规划。

Theta*（2007年）：A* 的一种变体，能够提供比 Field D* 更优（更短）的路径。然而，由于其基于 A* 而非 D* Lite，因此不具备 Field D* 所具有的快速重规划能力。另请参阅相关文献。

Incremental Phi*（2009年）：兼具两者之长。Theta* 的增量版本（即支持快速重规划）。

移动目标点

GAA*（2008年）：GAA*（Generalized Adaptive A*）是 A* 的一种变体，专门用于处理运动目标点场景。这是更早的算法"Moving Target Adaptive A*"的泛化推广。

GFRA*（2010年）：GFRA*（Generalized Edge Retrieval A*）似乎是 GAA* 的进一步泛化，通过使用另一种称为 FRA* 的算法，将其适用范围拓展至任意图结构（即不限于二维网格）。

MTD*-Lite（2010年）：MTD*-Lite（Moving Target D* Lite）是"D* Lite 的扩展，它使用 Generalized Edge Retrieval A* 背后的原理"来实现面向移动目标的高效重规划搜索。

Tree-AA*（2011年）：（待考证）似乎是一种用于未知地形搜索的算法，但与本小节中的所有其他算法一样，它同样基于 Adaptive A*，因此在此一并列出。与本节中其他算法的对比尚不明确。

快速/次优

Anytime D*（2005年）：这是 D* Lite 的"随时"变体，通过将 D* Lite 与称为 Anytime Repairing A* 的算法相结合而实现。随时算法是一种可在任意时间约束下运行的算法——它能够迅速找到一条初始的次优路径作为起点，然后在给定更多时间的情况下，对该路径进行持续改进。

HPA*（2004年）：HPA*（Hierarchical Pathfinding A*）专为在大型图上为大量单元（例如 RTS 实时策略视频游戏中的单位）寻找路径而设计。这些单元各自具有不同的起始位置，且可能具有不同的目标位置。HPA* 将图分解为层次结构，从而能够快速找到所有这些单元的"接近最优"路径，其速度远胜于在每个单元上单独运行 A* 的方案。另请参阅相关文献。

PRA*（2005年）：据笔者理解，PRA*（Partial Refinement A*）解决了与 HPA* 相同的问题，但采用了不同的实现方式。两者具有"相似的性能特征"。

HAA*（2008年）：HAA*（Hierarchical Annotated A*）是 HPA* 的泛化推广，允许限制某些单元在某些地形上的通行能力（例如，某些通道大型单位无法通过而小型单位则可以；或仅飞行单位能够穿过的孔洞等）。

其他/未知

LPA（1997年）：LPA（Loop-free Pathfinding Algorithm）似乎是一种路由算法，与本节中其他算法所解决的问题仅存在轻微关联。笔者在此提及它，仅因为该论文在互联网上多处被混淆地（且错误地）引用为介绍 LPA* 的文献，实则并非如此。

LEARCH（2009年）：LEARCH 是一组机器学习算法的组合，用于教导机器人如何自主寻找接近最优的路径。作者建议将 LEARCH 与 Field D* 结合使用以获得更优效果。

BDDD*（2009年）：（待考证）笔者无法获取该论文。

SetA*（2002年）：（待考证）这显然是 A* 的一种变体，用于搜索图的"二元决策图"（BDD）模型。据称在某些情况下，其运行速度"比 A* 快数个数量级"。然而，若笔者的理解正确，这些情况是指图中每个节点均具有大量边的场景。

综合上述分析，LPA* 似乎最适合笔者所面临的问题。

\```
