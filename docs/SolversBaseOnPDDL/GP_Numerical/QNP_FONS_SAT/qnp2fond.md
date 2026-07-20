[TOC]

# qnp2fond

```
./qnp2fond [--force-direct] [--disable-optimizations] <qnp-file> <num-bits-per-counter> <max-stack-depth> <prefix>
```

例子

```
$ ./qnp2fond ./blocks04.qnp 2 2  blocks04_output
call: ./qnp2fond ./blocks04.qnp 2 2 blocks04_output
qnp: #features=5, #numeric=2, #boolean=3, #actions=8
using full translation...
translation: time=0
translation: stats.extra=[ 9 8 4 2 2 ]
fond: #features=22, #actions=16
```

有充分理由认为，pddl2cnf 翻译模块是经过充分验证的现有代码组件，其输入输出接口已经相当明确和成熟。

```
/hush$ diff ./FOND-SAT/src/translate/translate.py ./PRP/planner-for-relevant-policies/src/translate/translate.py
651,652d650
<         "sas_name", help="sas file name")
<     argparser.add_argument(
659d656
<     print('HOLAAAAAAAAAAAAAAAAAAAAAAA')
686c683
<         with open(args.sas_name, "w") as output_file:
---
>         with open("output.sas", "w") as output_file:
```

命令行执行：

```
command = 'python translate/translate.py ' + str(time_limit) + ' ' + self.domain + ' ' + self.problem + ' ' + sas_file_name + ' | grep "noprint"'
```

利用领域定义文件（domain.pddl）和问题描述文件（problem.pddl），通过 translate.py 脚本生成翻译后的中间表示文件（SAS 格式）

```
begin_version
3
end_version
begin_metric
0
end_metric
1
begin_variable
var0
-1
2
Atom person-at(l1)
Atom person-at(l2)
end_variable
1
begin_mutex_group
2
0 0
0 1
end_mutex_group
begin_state
0
end_state
begin_goal
1
0 1
end_goal
2
begin_operator 所有操作符均在此处定义，例如 L3 场景下共包含 4 个操作
move-right l1 l2
0
1
0 0 0 1
0
end_operator
begin_operator
move-right l2 l1
0
1
0 0 1 0
0
end_operator
0 此行为固定格式结尾标记
```

接着

```
p.generate_task(name_sas_file) # 读取 SAS 文件，解析并保存结构化的规划数据
>>> my_task = p.translate_to_atomic() # 将解析后的数据存储至 MyTask 类的实例对象 my_task 中
```
