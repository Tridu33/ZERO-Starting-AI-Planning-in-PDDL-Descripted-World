## PDDL简介

en.wikipedia.org/wiki/Planning_Domain_Definition_Language

https://dblp.uni-trier.de/search?q=pddl

[Writing Planning Domains and Problems in PDDL](http://users.cecs.anu.edu.au/~patrik/pddlman/writing.html)

en.wikipedia.org/wiki/Planning_Domain_Definition_Language

古典计划使用从STRIPS建模语言[Richard E Fikes and Nils J Nilsson.  Strips: A new approach to the application of theorem proving to problemsolving.Artificial intelligence, 2(3-4):189–208, 1971]派生而来的正式描述语言，称为计划领域定义语言（PDDL）[Drew McDermott, Malik Ghallab, Adele Howe, Craig Knoblock, Ashwin Ram, Manuela Veloso, Daniel Weld,and David Wilkins. Pddl-the planning domain definition language, 1998.]


我们关注的是令人满意的计划任务，它可以由集合（F，O，I，G）定义，其中F是一组命题（或谓词），它们描述任务实例中存在的对象的属性及其关系，O是一组运算符（或操作类型），ICF是初始状态，而GCF是目标状态的集合。每个动作类型GO都由三元组（Pre（o），Add（o），Del（o））定义，其中前提为Pre（o）是一组谓词，这些谓词必须具有正确的值才能适用于该操作，Add（o）是一组谓词，在应用后该行为将变为真，而Del（o）是一组谓词，该行为将变为false根据申请。我们试图找到一个计划或一系列行动，这些行动或行动序列一旦应用，就会在一定时限或预定数量的步骤内导致状态为G C的状态。查找计划任务的计划通常是通过启发式搜索方法来完成的，但是，在这项工作中，我们专注于学习反应式计划策略，这些策略可以在特定领域的实例上进行训练，然后推广到同一领域中新的看不见的实例。

人工智能领域语言中PDDL 和Prolog

https://www.metalevel.at/prolog/showcases/turing.pl

简介：PDDL是一种用于表达计划任务的领域特定语言，而Prolog是一种成熟的编程语言，可让您表达所有可能的计算（包括解决计划任务）。

https://www.quora.com/What-is-difference-in-expressive-power-between-PDDL-and-Prolog


PDDL代表规划域定义语言。它是用于计划任务的标准编码。请注意，PDDL有不同版本，并且具有各种扩展名。

实际上，许多“ PDDL”求解器仅支持PDDL的某些子集。

通常，对计划任务的描述由特定组件组成，例如：

> 初始状态
> 一个目标
> 可以执行的动作
> 等

如果您的计划框架足够通用，那么这种特定于领域的计划语言实际上可以是**Turing-complete** ，因此与通用编程语言（例如Prolog）具有相同的计算能力：证明图灵机领域可以看作是经典的计划领域。

但是，PDDL并非如此：在PDDL中，通常需要对某些有限域（例如整数的有限间隔）进行推理。如果域是有限的，则无法建模无限的磁带，因此PDDL的表达能力**明显低于**Prolog。

此外，您通常只对多项式长度的计划感兴趣，甚至仅限于多项式长度的计划。在这种情况下，PDDL是PSPACE或EXPTIME完整的，具体取决于您使用的扩展名和变体。这尤其意味着**存在许多无法在PDDL中表达的计算任务**。

从实践的角度来看，即使PDDL在理论上足够强大，可以对所有计算任务进行建模，但在计划任务的预期应用领域之外使用它是否是方便或可取的仍值得商榷，所以用pddl描述自动机推演生成policy算法控制流图解子图"程序综合"可能需要PDDL的扩展版本或者基于其上做写framwork。

另一方面，Prolog是图灵完备的编程语言。这尤其意味着你可以表现一切任何编程语言，你可以也表达序言。您可以通过使用Prolog模拟图灵机来显示此信息：

以下是一些其他参考资料，希望对您有用：

https://www.cs.toronto.edu/~sheila/2542/s14/A1/introtopddl2.pdf

## 在PDDL中编写计划领域和问题

PDDL背景

http://homepages.inf.ed.ac.uk/mfourman/tools/propplan/pddl.pdf

http://users.cecs.anu.edu.au/~thiebaux/papers/ijcai03.pdf

https://fai.cs.uni-saarland.de/hoffmann/papers/ki11.pdf

在线 https://editor.planning.domains/# PDDL编辑器

















