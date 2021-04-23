#  solver汇总

## IPC比赛---故事开始的地方

https://www.icaps-conference.org/competitions/  汇总每一届比赛链接


An Overview of theInternational Planning Competition   chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://www.nms.kcl.ac.uk/andrew.coles/PlanningCompetitionAAAISlides.pdf


https://helios.hud.ac.uk/scommv/IPC-14/selection.html 2014


International Planning Competition

https://ipc2018-classical.bitbucket.io/ 2018


eecs.oregonstate.edu/ipc-learn/ 6

cs.cmu.edu/afs/cs/project/jair/pub/volume20/long03a-html/node2.html
  国际规划大赛系列



主要分：

古典规划：一个实例一个解；

通用规划：多个实例共用一个解子图算法Control Flow Graph，常见的有QNP,FOND

## CP古典规划

FF

FD

LPKT

## GP通用规划



- MyND

- PRP

- FOND-SAT

- PRP_planner-for-relevant-policies



宏观来看，一般两条路：

Top-Down(与或树{或者也可以理解为ControlFlowGraph}在图中搜索-->algorithm-like 的policy，在我看来，这就是符号化goto语句的底层汇编算法等价描述) 



&& 



Bottom-Up(生成实例经典规划中完善补全抽象图，不断响应式打补丁)，FONS-SAT可以看作文法自动机，用符号SAT可满足性求解，就我的理解来说，其实属于Top-Down“求解”。

如：Merging Example Plans into Generalized Plans forNon-deterministic Environments和Directed Search for Generalized Plans Using Classical Planners

> 正如Dijkstra在他书中说到意思，编程是严谨思考推理得到的算法，而不应该是意大利苗条代码中盲目debug函试错，疯狂为特殊情况打补丁。
>
> 图灵开启的自动编程故事，相信plan会是一个美丽的解法。

QNP其实就是在模拟有while循环的Linked list reverse受到的启发，才提出来的，这类问题的解子图policy其实就是**包含while循环的algorithm**。

实例中学习，就比可避免要考虑**覆盖率**(计划问题总数中已解决问题的数目)，我们设想如果有一个比较完善的GP良定义，这个结果应该是完善的自顶向下的精巧设计，而不是草草上线不断打补丁的缝合怪(尽管多数时间是这么做的)

一个比较合适的算法例子是三数之和：

> 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
>
> 注意：答案中不可以包含重复的三元组。
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

注意上述这个例子：

> 错误去重方法将会漏掉-1,-1,2 这种情况；去重复逻辑放置位置，0，0，0 的情况 。

给我们的启发是正如dijkstra在他的著作中写到的，top-down精巧的设计才能做出不是玩具可用性鲁棒性强的算法解。

而这，恰恰是实例CP中学习GP抽象图不断打补丁的bottom-up方法中学不到的东西，这样实例CP中学习的GP抽象控制流图只会千疮百孔打满补丁，甚至还不能AC满足足够的测例覆盖率。

##  为什么我认为CFG控制图是最佳中间intermediate representation表示方法

## Planning Graph Analysis

Fast planning through planning graph analysis 1997

https://dblp.uni-trier.de/pid/b/AvrimBlum.html 作者主页

2003 SAT-Based Model-Checking of Security Protocols Using Planning Graph Analysis. 

2006

2017 

link.springer.com/chapter/10.1007%2F3-540-46238-4_31

On Plan Adaptation through Planning Graph Analysis

A Planning Heuristic Based on Causal Graph Analysis 2004

aaai.org/Library/ICAPS/2004/icaps04-021.php

这些问题对于基于计划图（例如IPP，Graphplan和Blackbox）的当前计划者

## 图最新路径查找算法

用于更改图形（D *，D * -Lite，LPA *等）的最新路径查找算法有何不同？

https://qastack.cn/cstheory/11855/how-do-the-state-of-the-art-pathfinding-algorithms-for-changing-graphs-d-d-l

我到目前为止能够找到的：

\```

D *（1994）

专注D *（1995）

动态SWSF-FP（1996）

LPA（1997）

LPA * /增量A *（2001）

D * Lite（2002）

SetA *（2002年）

HPA *（2004）

随时D *（2005）

PRA *（2005年）

领域D *（2007）

Theta *（2007）

HAA *（2008）

GAA *（2008）

LEARCH（2009）

BDDD *（2009年-我无法访问本文：|）

增量披披*（2009）

GFRA *（2010）

MTD * -Lite（2010）

树AA *（2011）

\```









可以在上方的问题栏中找到每篇论文的链接。



简单的重新计算



\```

D * （又名Dynamic A *）（1994年）：在最初的运行中，D *的运行与A *非常相似，因此可以非常迅速地找到从头到尾的最佳路径。但是，随着单元从头到尾移动，如果图形发生变化，D *能够非常快速地重新计算从该单元位置到终点的最佳路径，这比再次从该单元位置简单地运行A *快得多。但是，D *以极其复杂而著称，而更简单的D * -Lite已完全淘汰了D *。

聚焦D *（1995年）：对D *的改进，使其更快/“更实时”。我找不到与D * -Lite的任何比较，但是鉴于它比较老，并且D * -Lite的讨论更多，我认为D * -Lite更好。

DynamicSWSF-FP（1996）：存储从每个节点到完成节点的距离。具有较大的初始设置以计算所有距离。更改图形后，它只能更新距离已更改的节点。与A *和D *无关。当您要查找每次更改后从多个节点到终点的距离时很有用；否则，LPA *或D * -Lite通常更有用。

LPA * / Incremental A *（2001）：LPA * （终身计划A *），也称为Incremental A * （有时令人困惑，也称为“ LPA”，尽管它与其他名为LPA的算法无关）是DynamicSWSF-FP和A *的组合。在第一次运行时，它与A *完全相同。但是，在对图形进行较小的更改后，与A *相比，从同一开始/完成对中进行后续搜索就可以使用先前运行中的信息来大大减少需要检查的节点数量。这正是我的问题，所以听起来LPA *将是我的最佳选择。LPA *与D *的不同之处在于，它总是找到从同一起点到同一终点的最佳路径。起点移动时不使用（例如沿初始最佳路径移动的单位）。然而...

D * -Lite（2002）：此算法使用LPA *模仿D *；也就是说，当它沿着初始最佳路径移动并且图形发生变化时，它会使用LPA *查找该单元的新最佳路径。D * -Lite被认为比D *简单得多，并且由于它始终至少与D *一样快地运行，因此它已经完全废弃了D *。因此，从没有任何理由使用D *。改用D * -Lite。

任何角度的运动

字段D *（2007年）：D * -Lite的一种变体，不限制移动到网格；也就是说，最佳路径可以使单位沿任意角度移动，而不仅仅是网格点之间的45度（或90度）。被美国国家航空航天局（NASA）用来寻找火星探测器。

Theta *（2007）：A *的一种变体，比Field D *提供更好（更短）的路径。但是，由于它基于A *而不是D * -Lite，因此它没有Field D *所具有的快速重新计划功能。 另请参阅。

Incremental Phi *（2009）：两全其美。Theta *的一个增量版本（又名允许快速重新计划）

移动目标点

GAA *（2008年）：GAA * （广义自适应A *）是A *的一种变体，用于处理运动目标点。这是甚至更早的算法“运动目标自适应A *”的概括

GRFA *（2010）：GFRA * （广义边缘检索A *）似乎是（GA）* ，它是使用另一种称为FRA *的算法将GAA *概括为任意图形（即，不限于2D）的图。

MTD * -Lite（2010）：MTD * -Lite （移动目标D * -Lite）是“ D * Lite的扩展，它使用广义边缘检索A *背后的原理”来进行快速重新计划的移动目标搜索。

Tree-AA *（2011）：（???）似乎是一种用于搜索未知地形的算法，但与本节中的所有其他算法一样，它也是基于Adaptive A *的，因此在此将其放在此处。不确定与本节中的其他内容相比。

快速/次优

随时D *（2005）：这是D * -Lite 的“随时”变体，通过将D * -Lite与称为Anytime Repairing A *的算法结合使用来完成。“随时”算法是一种可以在任何时间限制下运行的算法-它会非常快地找到一条非常不理想的路径作为起点，然后在给出更多时间的情况下对该路径进行改进。

HPA *（2004年）：HPA * （分级路径查找A *）用于在大型图形上查找大量单位，例如RTS （实时策略）视频游戏。它们都将具有不同的开始位置，并且可能具有不同的结束位置。HPA *将图分成层次结构，以便快速找到所有这些单元的“接近最佳”路径，比在每个单元上单独运行A *要快得多。 也可以看看

PRA *（2005年）：据我了解，PRA * （部分优化A *）解决了与HPA *相同的问题，但是方式不同。它们都具有“相似的性能特征”。

HAA *（2008）：HAA * （分层注释A *）是HPA *的概括，它允许在某些地形上限制某些单元的穿越（例如，某些单元可以穿过而较小的通道则无法通过；或只有飞行单位可以穿过的孔；等等）

其他/未知

LPA（1997）：LPA （无环路路径查找算法）似乎是一种路由算法，仅与此处其他算法解决的问题略相关。我之所以仅提及它，是因为该论文在介绍LPA *的论文中在Internet上的多个地方被混淆（并且错误地）引用，而并非如此。

LEARCH（2009）：LEARCH是机器学习算法的组合，用于教机器人如何自行寻找接近最佳的路径。作者建议将LEARCH与Field D *结合使用以获得更好的结果。

BDDD *（2009）：??? 我无法获取论文。

SetA *（2002）：??? 显然，这是A *的一种变体，可以搜索图的“二进制决策图”（BDD）模型？他们声称它在某些情况下的运行“比A *快几个数量级”。但是，如果我理解正确，那么这些情况是图上的每个节点都有很多边吗？

考虑到所有这些，LPA *似乎最适合我的问题。



\```