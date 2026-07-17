# SGPlan6

SGPlan6 系伊利诺伊大学最新研发的智能规划器，在第五届国际规划大赛中荣获次优规划器冠军。该系统采用 Linux 平台下的 C++ 语言进行设计，需借助 Flex 与 Bison 工具以实现对 PDDL 的编译功能。

http://www.pudn.com/Download/item/id/2027508.html

## Sensory GraphPlan 主页

aiweb.cs.washington.edu/ai/sgp.html

web.cs.wpi.edu/~nth/cs534/resources/SensoryGraphPlan/sgp/

1998 年，Daniel S. Weld、Corin R. Anderson 与 David E. Smith 共同提出了感知图规划算法（Sensory GraphPlan, SGP）。感知图规划算法兼具优势与不足，其缺点主要包括：算法结构较为复杂且时间复杂度较高；不具备启发式搜索能力，搜索过程从初始状态出发，遍历所有可能为真的命题，导致效率低下。上述因素致使 SGP 规划器的整体性能不甚理想。为克服感知图规划的局限性，相关研究提出了一种基于启发式搜索的感知图规划算法。《一种基于启发式搜索的感知图规划算法的研究与实现》中阐述了一种新型算法。该算法有别于既有方法，采用了 FF 规划器中所使用的启发式方法，同时吸纳了 FF 中的松弛动作（relaxed action）策略。因此，在图扩张阶段无需处理互斥关系，极大地提升了算法效率。本文所提出的方法有效提高了规划器的求解能力，对理论研究与工程应用均具有重要的参考价值。
