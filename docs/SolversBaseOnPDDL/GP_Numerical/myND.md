follow作者一下先
https://github.com/robertmattmueller



# myND
JRE 1.6

java [https://github.com/robertmattmueller/myND/blob/master/README.rst](https://github.com/robertmattmueller/myND/blob/master/README.rst)


https://github.com/robertmattmueller/myND


报错

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

在Java的早期版本中，下划线可以用作标识符，也可以用来创建变量名。但是在Java 9发行版中，下划线是关键字，不能用作标识符或变量名。

如果我们使用下划线字符（“ _”）作为标识符，则无法再编译我们的源代码








Gamer

while we obtained Gamer from the authors of MyND.

## sdac-compiler
https://github.com/robertmattmueller/sdac-compiler

使用基于EVMDD的操作编译将具有状态相关操作成本的PDDL任务编译为具有状态独立成本的任务

该编译器根据带有边值多值决策图（EVMDD）的动作编译，处理带有状态相关动作成本的PDDL问题，并生成具有固定成本的PDDL问题，如[*删除带有状态的计划的松弛方案中*](http://gki.informatik.uni-freiburg.de/papers/geisser-etal-ijcai2015.pdf)所述。 [*相依行动成本*](http://gki.informatik.uni-freiburg.de/papers/geisser-etal-ijcai2015.pdf)。

一个例子PDDL域文件可以发现[这里](https://raw.githubusercontent.com/robertmattmueller/sdac-compiler/master/example/domain-sdac.pddl)和成本函数的BNF语法，可以发现[在这里](https://github.com/robertmattmueller/sdac-compiler/blob/master/documents/bnf.pdf)。请注意，编译器当前不支持实数，并且forall / exists语言构造。

感谢Christian Muise，我们也为Planning.Domains编辑器提供了一个有效的插件。[该](http://editor.planning.domains/#http://www.haz.ca/tutorial2.js)链接立即加载编译器插件，并使用lm-cut将基础计划程序更改为Fast Downward。请注意，在线编译器有**15秒的超时时间**，对于复杂的成本函数，请记住这一点。

## EVMDD Library for Python (pyevmdd)

[EVMDD Library for Python (pyevmdd)](https://github.com/robertmattmueller/pyevmdd)



这个小项目的目的是提供一个轻量级的纯Python EVMDD库。它仍处于发展的初期。












