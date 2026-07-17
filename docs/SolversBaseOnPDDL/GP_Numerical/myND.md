敬请关注作者：
https://github.com/robertmattmueller

# myND

JRE 1.6

Java 实现，仓库地址：[https://github.com/robertmattmueller/myND/blob/master/README.rst](https://github.com/robertmattmueller/myND/blob/master/README.rst)

https://github.com/robertmattmueller/myND

**编译报错信息：**

```
$ ./build
./main/java/javabdd/BDDFactory.java:40: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (AccessControlException _) {
                                    ^
./main/java/javabdd/BDDFactory.java:88: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (ClassNotFoundException _) {
                                    ^
./main/java/javabdd/BDDFactory.java:89: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (NoSuchMethodException _) {
                                   ^
./main/java/javabdd/BDDFactory.java:90: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (IllegalAccessException _) {
                                    ^
./main/java/javabdd/BDDFactory.java:91: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (InvocationTargetException _) {
                                       ^
./main/java/javabdd/BDDFactory.java:565: error: as of release 9, '_' is a keyword, and may not be used as an identifier
        } catch (IOException _) {
                             ^
./main/java/javabdd/BDDFactory.java:735: error: as of release 9, '_' is a keyword, and may not be used as an identifier
        } catch (IOException _) {
                             ^
./main/java/javabdd/FindBestOrder.java:213: error: as of release 9, '_' is a keyword, and may not be used as an identifier
          } catch (IOException _) {
                               ^
./main/java/javabdd/TryVarOrder.java:71: error: as of release 9, '_' is a keyword, and may not be used as an identifier
          } catch (IOException _) {
                               ^
./net/sf/javabdd/BDDFactory.java:40: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (AccessControlException _) {
                                    ^
./net/sf/javabdd/BDDFactory.java:88: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (ClassNotFoundException _) {
                                    ^
./net/sf/javabdd/BDDFactory.java:89: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (NoSuchMethodException _) {
                                   ^
./net/sf/javabdd/BDDFactory.java:90: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (IllegalAccessException _) {
                                    ^
./net/sf/javabdd/BDDFactory.java:91: error: as of release 9, '_' is a keyword, and may not be used as an identifier
    } catch (InvocationTargetException _) {
                                       ^
./net/sf/javabdd/BDDFactory.java:565: error: as of release 9, '_' is a keyword, and may not be used as an identifier
        } catch (IOException _) {
                             ^
./net/sf/javabdd/BDDFactory.java:735: error: as of release 9, '_' is a keyword, and may not be used as an identifier
        } catch (IOException _) {
                             ^
./net/sf/javabdd/FindBestOrder.java:213: error: as of release 9, '_' is a keyword, and may not be used as an identifier
          } catch (IOException _) {
                               ^
./net/sf/javabdd/TryVarOrder.java:71: error: as of release 9, '_' is a keyword, and may not be used as an identifier
          } catch (IOException _) {
                               ^
```

https://www.javatpoint.com/java-9-underscore-keyword

在 Java 的早期版本中，下划线可用作标识符，亦可用来创建变量名。然而，自 Java 9 发行版起，下划线已被纳入关键字范畴，不得再作为标识符或变量名使用。

若将下划线字符（"_"）用作标识符，则源代码将无法通过编译。

## Gamer

我们从 MyND 的原作者处获取了 Gamer。

## sdac-compiler

https://github.com/robertmattmueller/sdac-compiler

**基于 EVMDD 的操作编译：将具有状态相关操作成本的 PDDL 任务编译为具有状态独立成本的任务**

该编译器依据基于边值多值决策图（Edge-Valued Multi-Valued Decision Diagram, EVMDD）的动作编译机制，处理带有状态相关动作成本的 PDDL 问题，并生成具有固定成本的 PDDL 问题，其理论依据详见《*删除带有状态依赖行动成本的计划的松弛方案*》（Geisser 等，IJCAI 2015）。

示例 PDDL 领域文件可参见[此处](https://raw.githubusercontent.com/robertmattmueller/sdac-compiler/master/example/domain-sdac.pddl)，代价函数的 BNF 语法可参见[此处](https://github.com/robertmattmueller/sdac-compiler/blob/master/documents/bnf.pdf)。请注意，当前编译器暂不支持实数类型以及 forall/exists 语言构造。

感谢 Christian Muise，我们还为 Planning.Domains 编辑器提供了可正常运行的插件。[该链接](http://editor.planning.domains/#http://www.haz.ca/tutorial2.js)可直接加载编译器插件，并采用 lm-cut 将基础规划器切换为 Fast Downward。请注意，在线编译器设有 **15 秒的超时限制**，对于复杂的代价函数请务必注意这一点。

## EVMDD Library for Python (pyevmdd)

[EVMDD Library for Python (pyevmdd)](https://github.com/robertmattmueller/pyevmdd)

此项目的目标在于提供一个轻量级的纯 Python EVMDD 库。目前该项目仍处于早期开发阶段。
