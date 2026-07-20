# MyND 规划器

> 作者主页：[Robert Mattmueller](https://github.com/robertmattmueller)

## 项目概览

MyND 是一个基于 Java 实现的通用规划器，需 JRE 1.6 环境运行。

- [GitHub 仓库](https://github.com/robertmattmueller/myND)
- [README 文档](https://github.com/robertmattmueller/myND/blob/master/README.rst)

## 编译问题

在 Java 9 及以上版本中编译时，由于下划线（`_`）在 Java 9 中被列为关键字，无法再作为标识符使用，会导致编译错误：

```
$ ./build
./main/java/javabdd/BDDFactory.java:40: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (AccessControlException _) {
                                    ^
./main/java/javabdd/BDDFactory.java:88: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (ClassNotFoundException _) {
                                    ^
```

该问题涉及 `BDDFactory.java`、`FindBestOrder.java`、`TryVarOrder.java` 等多个源文件，共计 18 处类似的 catch 语句语法错误。详见 [Java 9 下划线关键字说明](https://www.javatpoint.com/java-9-underscore-keyword)。

在 Java 的早期版本中，下划线可用作标识符，亦可用来创建变量名。然而，自 Java 9 发行版起，下划线已被纳入关键字范畴，不得再作为标识符或变量名使用。若将下划线字符（"_"）用作标识符，则源代码将无法通过编译。

## Gamer

我们从 MyND 的原作者处获取了 Gamer。

## sdac-compiler

[sdac-compiler 仓库](https://github.com/robertmattmueller/sdac-compiler)

**基于 EVMDD 的操作编译：将具有状态相关操作成本的 PDDL 任务编译为具有状态独立成本的任务**

该编译器依据基于边值多值决策图（Edge-Valued Multi-Valued Decision Diagram, EVMDD）的动作编译机制，处理带有状态相关动作成本的 PDDL 问题，并生成具有固定成本的 PDDL 问题，其理论依据详见《删除带有状态依赖行动成本的计划的松弛方案》（Geisser 等，IJCAI 2015）。

[示例 PDDL 领域文件](https://raw.githubusercontent.com/robertmattmueller/sdac-compiler/master/example/domain-sdac.pddl)，[代价函数的 BNF 语法](https://github.com/robertmattmueller/sdac-compiler/blob/master/documents/bnf.pdf)。请注意，当前编译器暂不支持实数类型以及 forall/exists 语言构造。

感谢 Christian Muise，我们还为 [Planning.Domains 编辑器](http://editor.planning.domains/#http://www.haz.ca/tutorial2.js)提供了可正常运行的插件。该链接可直接加载编译器插件，并采用 lm-cut 将基础规划器切换为 Fast Downward。请注意，在线编译器设有 **15 秒的超时限制**，对于复杂的代价函数请务必注意这一点。

## EVMDD Library for Python (pyevmdd)

[pyevmdd 仓库](https://github.com/robertmattmueller/pyevmdd)

此项目的目标在于提供一个轻量级的纯 Python EVMDD 库。目前该项目仍处于早期开发阶段。
