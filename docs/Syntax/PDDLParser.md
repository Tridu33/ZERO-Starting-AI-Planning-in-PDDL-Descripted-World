# PDDL 解析器总览

PDDL 的 BNF 文法描述可参见 [PDDL3 标准文法](https://github.com/nergmada/planning-wiki/blob/master/_citedpapers/pddl3bnf.pdf)。

[PDDL GitHub 仓库合集](https://github.com/topics/pddl) 中收录了多种解析器实现，按语言分类概览如下。

## Python

### pddl-lib

[pddl-lib](https://github.com/hfoffani/pddl-lib) 是一个基于 **ANTLR 4** 语法解析 PDDL 文件的库，提供了简洁的接口以支持领域问题（domain problems）的交互操作。该库公开了一个对象类，其 API 提供了以下方法以获取相应内容：

- 初始状态（initial state）
- 目标状态（goal）
- 运算符列表（operators）
- 正面与负面先决条件（positive and negative preconditions）及正面与负面效应（positive and negative effects）
- 给定算子的基例化（grounded）状态，涵盖基例化变量、前提条件与影响

借助该库，用户可专注于状态空间或规划空间搜索算法的实现。

```bash
pip install pddlpy
```

### universal-pddl-parser

由西班牙研究团队开发的 [universal-pddl-parser](https://github.com/wisdompoet/universal-pddl-parser) 提供了一种适用于任意 PDDL 格式规划问题的通用解析算法。当前支持 STRIPS 规划、时间规划及多智能体规划，基于 Scons 构建。

### ply-pddl-parser

[ply-pddl-parser](https://github.com/makintunde/ply-pddl-parser) 是一个基于 PLY 编写的 PDDL 解析器。

### pddl-parser-2

[pddl-parser-2](https://github.com/boompig/pddl-parser-2) 是一组用于读取 PDDL 及 POND（Partially-Observable Non-Deterministic）文件的实用工具集合。

## Java

- [pddl-parser (Java)](https://github.com/gerryai/pddl-parser)

## JavaScript

### pddl2json

该项目致力于构建基于 [PEG.js](https://pegjs.org/online) 的基本 STRIPS PDDL 语法解析器，作为学习示例，展示如何将 PDDL 转换为 JSON 结构化数据。

相关示例参见 [PDDL 转 JSON 示例 Gist](https://gist.github.com/primaryobjects/22363e71112d716ea183)。

```bash
pip install pddlpy   # PDDL 解析器
# 将 PDDL 文件读取至内存，转换为 Python 可访问的结构化数据格式
# pddl2json 函数负责将其输出转换为 JSON 结构；在网络编程中，JSON 几乎是 JavaScript 的唯一选择
```

## 参考资源

- [UPF 通用 PDDL 解析器官方页面](https://www.upf.edu/web/ai-ml/universal-pddl-parser) — 庞培法布拉大学（UPF）人工智能与机器学习研究小组（位于西班牙巴塞罗那）
- AIG 软件资料库
