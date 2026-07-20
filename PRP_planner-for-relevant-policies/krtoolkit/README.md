# KR Toolkit

Various libraries to help with common AI research in knowledge representation and reasoning.

## Disclaimer
The KR Toolkit was written in a time where much of its functionality didn't exist. The future of the library is to branch out the useful and unique contributions into their own libraries, and let the entire library be deprecated. For archival purposes, the list of [issues](https://github.com/QuMuLab/krtoolkit/issues) and main [wiki pages](https://github.com/QuMuLab/krtoolkit/wiki) have been ported from the original repository on BitBucket. If you are interested in any aspect of the functionality, [let me know](http://www.haz.ca/).



```
tridu33@tridu33:/mnt/d/tridu33/postgraduate/QNP_GP/GP-QNP-FONDSAS+_Solvers/PRP_planner-for-relevant-policies/krtoolkit$ sudo python setup.py install
[sudo] password for tridu33:
running install
running build
running build_py
running install_lib
creating /usr/local/lib/python2.7/dist-packages/krrt
creating /usr/local/lib/python2.7/dist-packages/krrt/planning
creating /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/actions.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/axioms.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/build_model.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/conditions.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/effects.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/functions.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/f_expression.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/graph.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/greedy_join.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/instantiate.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/normalize.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/parser.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/pddl_file.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/pddl_to_prolog.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/pddl_types.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/predicates.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/pretty_print.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/split_rules.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/tasks.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/timers.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/tools.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
copying build/lib.linux-x86_64-2.7/krrt/planning/pddl/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl
creating /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/cg.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/dtg.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/extra.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/group_keys.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/mutex_groups.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/myiterators.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/sas_tasks.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/statistics.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/switch_graph.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
copying build/lib.linux-x86_64-2.7/krrt/planning/sas/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/sas
creating /usr/local/lib/python2.7/dist-packages/krrt/planning/strips
copying build/lib.linux-x86_64-2.7/krrt/planning/strips/reasoning.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/strips
copying build/lib.linux-x86_64-2.7/krrt/planning/strips/representation.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/strips
copying build/lib.linux-x86_64-2.7/krrt/planning/strips/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning/strips
copying build/lib.linux-x86_64-2.7/krrt/planning/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/planning
creating /usr/local/lib/python2.7/dist-packages/krrt/sat
copying build/lib.linux-x86_64-2.7/krrt/sat/CNF.py -> /usr/local/lib/python2.7/dist-packages/krrt/sat
copying build/lib.linux-x86_64-2.7/krrt/sat/dDNNF.py -> /usr/local/lib/python2.7/dist-packages/krrt/sat
copying build/lib.linux-x86_64-2.7/krrt/sat/Dimacs.py -> /usr/local/lib/python2.7/dist-packages/krrt/sat
copying build/lib.linux-x86_64-2.7/krrt/sat/DPLL.py -> /usr/local/lib/python2.7/dist-packages/krrt/sat
copying build/lib.linux-x86_64-2.7/krrt/sat/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/sat
creating /usr/local/lib/python2.7/dist-packages/krrt/search
creating /usr/local/lib/python2.7/dist-packages/krrt/search/backtrack
creating /usr/local/lib/python2.7/dist-packages/krrt/search/backtrack/viz
copying build/lib.linux-x86_64-2.7/krrt/search/backtrack/viz/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/search/backtrack/viz
copying build/lib.linux-x86_64-2.7/krrt/search/backtrack/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/search/backtrack
creating /usr/local/lib/python2.7/dist-packages/krrt/search/localsearch
creating /usr/local/lib/python2.7/dist-packages/krrt/search/localsearch/viz
copying build/lib.linux-x86_64-2.7/krrt/search/localsearch/viz/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/search/localsearch/viz
copying build/lib.linux-x86_64-2.7/krrt/search/localsearch/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/search/localsearch
copying build/lib.linux-x86_64-2.7/krrt/search/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/search
creating /usr/local/lib/python2.7/dist-packages/krrt/stats
copying build/lib.linux-x86_64-2.7/krrt/stats/plots.py -> /usr/local/lib/python2.7/dist-packages/krrt/stats
copying build/lib.linux-x86_64-2.7/krrt/stats/tests.py -> /usr/local/lib/python2.7/dist-packages/krrt/stats
copying build/lib.linux-x86_64-2.7/krrt/stats/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/stats
creating /usr/local/lib/python2.7/dist-packages/krrt/utils
copying build/lib.linux-x86_64-2.7/krrt/utils/cmd_line.py -> /usr/local/lib/python2.7/dist-packages/krrt/utils
copying build/lib.linux-x86_64-2.7/krrt/utils/experimentation.py -> /usr/local/lib/python2.7/dist-packages/krrt/utils
copying build/lib.linux-x86_64-2.7/krrt/utils/fileio.py -> /usr/local/lib/python2.7/dist-packages/krrt/utils
copying build/lib.linux-x86_64-2.7/krrt/utils/result_handlers.py -> /usr/local/lib/python2.7/dist-packages/krrt/utils
copying build/lib.linux-x86_64-2.7/krrt/utils/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt/utils
copying build/lib.linux-x86_64-2.7/krrt/__init__.py -> /usr/local/lib/python2.7/dist-packages/krrt
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/actions.py to actions.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/axioms.py to axioms.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/build_model.py to build_model.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/conditions.py to conditions.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/effects.py to effects.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/functions.py to functions.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/f_expression.py to f_expression.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/graph.py to graph.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/greedy_join.py to greedy_join.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/instantiate.py to instantiate.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/normalize.py to normalize.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/parser.py to parser.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/pddl_file.py to pddl_file.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/pddl_to_prolog.py to pddl_to_prolog.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/pddl_types.py to pddl_types.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/predicates.py to predicates.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/pretty_print.py to pretty_print.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/split_rules.py to split_rules.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/tasks.py to tasks.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/timers.py to timers.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/tools.py to tools.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/pddl/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/cg.py to cg.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/dtg.py to dtg.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/extra.py to extra.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/group_keys.py to group_keys.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/mutex_groups.py to mutex_groups.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/myiterators.py to myiterators.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/sas_tasks.py to sas_tasks.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/statistics.py to statistics.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/switch_graph.py to switch_graph.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/sas/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/strips/reasoning.py to reasoning.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/strips/representation.py to representation.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/strips/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/planning/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/sat/CNF.py to CNF.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/sat/dDNNF.py to dDNNF.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/sat/Dimacs.py to Dimacs.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/sat/DPLL.py to DPLL.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/sat/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/search/backtrack/viz/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/search/backtrack/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/search/localsearch/viz/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/search/localsearch/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/search/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/stats/plots.py to plots.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/stats/tests.py to tests.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/stats/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/utils/cmd_line.py to cmd_line.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/utils/experimentation.py to experimentation.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/utils/fileio.py to fileio.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/utils/result_handlers.py to result_handlers.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/utils/__init__.py to __init__.pyc
byte-compiling /usr/local/lib/python2.7/dist-packages/krrt/__init__.py to __init__.pyc
running install_egg_info
Writing /usr/local/lib/python2.7/dist-packages/KR_Toolkit-0.1.egg-info
tridu33@tridu33:/mnt/d/tridu33/postgraduate/QNP_GP/GP-QNP-FONDSAS+_Solvers/PRP_planner-for-relevant-policies/krtoolkit$ sudo python3 setup.py install
running install
running build
running build_py
creating build/lib
creating build/lib/krrt
copying krrt/__init__.py -> build/lib/krrt
creating build/lib/krrt/sat
copying krrt/sat/CNF.py -> build/lib/krrt/sat
copying krrt/sat/dDNNF.py -> build/lib/krrt/sat
copying krrt/sat/Dimacs.py -> build/lib/krrt/sat
copying krrt/sat/DPLL.py -> build/lib/krrt/sat
copying krrt/sat/__init__.py -> build/lib/krrt/sat
creating build/lib/krrt/stats
copying krrt/stats/plots.py -> build/lib/krrt/stats
copying krrt/stats/tests.py -> build/lib/krrt/stats
copying krrt/stats/__init__.py -> build/lib/krrt/stats
creating build/lib/krrt/utils
copying krrt/utils/cmd_line.py -> build/lib/krrt/utils
copying krrt/utils/experimentation.py -> build/lib/krrt/utils
copying krrt/utils/fileio.py -> build/lib/krrt/utils
copying krrt/utils/result_handlers.py -> build/lib/krrt/utils
copying krrt/utils/__init__.py -> build/lib/krrt/utils
creating build/lib/krrt/planning
copying krrt/planning/__init__.py -> build/lib/krrt/planning
creating build/lib/krrt/planning/pddl
copying krrt/planning/pddl/actions.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/axioms.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/build_model.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/conditions.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/effects.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/functions.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/f_expression.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/graph.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/greedy_join.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/instantiate.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/normalize.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/parser.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/pddl_file.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/pddl_to_prolog.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/pddl_types.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/predicates.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/pretty_print.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/split_rules.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/tasks.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/timers.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/tools.py -> build/lib/krrt/planning/pddl
copying krrt/planning/pddl/__init__.py -> build/lib/krrt/planning/pddl
creating build/lib/krrt/planning/sas
copying krrt/planning/sas/cg.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/dtg.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/extra.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/group_keys.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/mutex_groups.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/myiterators.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/sas_tasks.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/statistics.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/switch_graph.py -> build/lib/krrt/planning/sas
copying krrt/planning/sas/__init__.py -> build/lib/krrt/planning/sas
creating build/lib/krrt/planning/strips
copying krrt/planning/strips/reasoning.py -> build/lib/krrt/planning/strips
copying krrt/planning/strips/representation.py -> build/lib/krrt/planning/strips
copying krrt/planning/strips/__init__.py -> build/lib/krrt/planning/strips
creating build/lib/krrt/search
copying krrt/search/__init__.py -> build/lib/krrt/search
creating build/lib/krrt/search/backtrack
copying krrt/search/backtrack/__init__.py -> build/lib/krrt/search/backtrack
creating build/lib/krrt/search/localsearch
copying krrt/search/localsearch/__init__.py -> build/lib/krrt/search/localsearch
creating build/lib/krrt/search/backtrack/viz
copying krrt/search/backtrack/viz/__init__.py -> build/lib/krrt/search/backtrack/viz
creating build/lib/krrt/search/localsearch/viz
copying krrt/search/localsearch/viz/__init__.py -> build/lib/krrt/search/localsearch/viz
running install_lib
creating /usr/local/lib/python3.6/dist-packages/krrt
creating /usr/local/lib/python3.6/dist-packages/krrt/planning
creating /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/actions.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/axioms.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/build_model.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/conditions.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/effects.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/functions.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/f_expression.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/graph.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/greedy_join.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/instantiate.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/normalize.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/parser.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/pddl_file.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/pddl_to_prolog.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/pddl_types.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/predicates.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/pretty_print.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/split_rules.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/tasks.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/timers.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/tools.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
copying build/lib/krrt/planning/pddl/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl
creating /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/cg.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/dtg.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/extra.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/group_keys.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/mutex_groups.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/myiterators.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/sas_tasks.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/statistics.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/switch_graph.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
copying build/lib/krrt/planning/sas/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/sas
creating /usr/local/lib/python3.6/dist-packages/krrt/planning/strips
copying build/lib/krrt/planning/strips/reasoning.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/strips
copying build/lib/krrt/planning/strips/representation.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/strips
copying build/lib/krrt/planning/strips/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning/strips
copying build/lib/krrt/planning/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/planning
creating /usr/local/lib/python3.6/dist-packages/krrt/sat
copying build/lib/krrt/sat/CNF.py -> /usr/local/lib/python3.6/dist-packages/krrt/sat
copying build/lib/krrt/sat/dDNNF.py -> /usr/local/lib/python3.6/dist-packages/krrt/sat
copying build/lib/krrt/sat/Dimacs.py -> /usr/local/lib/python3.6/dist-packages/krrt/sat
copying build/lib/krrt/sat/DPLL.py -> /usr/local/lib/python3.6/dist-packages/krrt/sat
copying build/lib/krrt/sat/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/sat
creating /usr/local/lib/python3.6/dist-packages/krrt/search
creating /usr/local/lib/python3.6/dist-packages/krrt/search/backtrack
creating /usr/local/lib/python3.6/dist-packages/krrt/search/backtrack/viz
copying build/lib/krrt/search/backtrack/viz/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/search/backtrack/viz
copying build/lib/krrt/search/backtrack/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/search/backtrack
creating /usr/local/lib/python3.6/dist-packages/krrt/search/localsearch
creating /usr/local/lib/python3.6/dist-packages/krrt/search/localsearch/viz
copying build/lib/krrt/search/localsearch/viz/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/search/localsearch/viz
copying build/lib/krrt/search/localsearch/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/search/localsearch
copying build/lib/krrt/search/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/search
creating /usr/local/lib/python3.6/dist-packages/krrt/stats
copying build/lib/krrt/stats/plots.py -> /usr/local/lib/python3.6/dist-packages/krrt/stats
copying build/lib/krrt/stats/tests.py -> /usr/local/lib/python3.6/dist-packages/krrt/stats
copying build/lib/krrt/stats/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/stats
creating /usr/local/lib/python3.6/dist-packages/krrt/utils
copying build/lib/krrt/utils/cmd_line.py -> /usr/local/lib/python3.6/dist-packages/krrt/utils
copying build/lib/krrt/utils/experimentation.py -> /usr/local/lib/python3.6/dist-packages/krrt/utils
copying build/lib/krrt/utils/fileio.py -> /usr/local/lib/python3.6/dist-packages/krrt/utils
copying build/lib/krrt/utils/result_handlers.py -> /usr/local/lib/python3.6/dist-packages/krrt/utils
copying build/lib/krrt/utils/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt/utils
copying build/lib/krrt/__init__.py -> /usr/local/lib/python3.6/dist-packages/krrt
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/actions.py to actions.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/axioms.py to axioms.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/build_model.py to build_model.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/conditions.py to conditions.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/effects.py to effects.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/functions.py to functions.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/f_expression.py to f_expression.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/graph.py to graph.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/greedy_join.py to greedy_join.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/instantiate.py to instantiate.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/normalize.py to normalize.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/parser.py to parser.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/pddl_file.py to pddl_file.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/pddl_to_prolog.py to pddl_to_prolog.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/pddl_types.py to pddl_types.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/predicates.py to predicates.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/pretty_print.py to pretty_print.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/split_rules.py to split_rules.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/tasks.py to tasks.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/timers.py to timers.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/tools.py to tools.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/pddl/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/cg.py to cg.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/dtg.py to dtg.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/extra.py to extra.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/group_keys.py to group_keys.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/mutex_groups.py to mutex_groups.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/myiterators.py to myiterators.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/sas_tasks.py to sas_tasks.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/statistics.py to statistics.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/switch_graph.py to switch_graph.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/sas/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/strips/reasoning.py to reasoning.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/strips/representation.py to representation.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/strips/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/planning/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/sat/CNF.py to CNF.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/sat/dDNNF.py to dDNNF.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/sat/Dimacs.py to Dimacs.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/sat/DPLL.py to DPLL.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/sat/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/search/backtrack/viz/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/search/backtrack/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/search/localsearch/viz/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/search/localsearch/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/search/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/stats/plots.py to plots.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/stats/tests.py to tests.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/stats/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/utils/cmd_line.py to cmd_line.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/utils/experimentation.py to experimentation.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/utils/fileio.py to fileio.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/utils/result_handlers.py to result_handlers.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/utils/__init__.py to __init__.cpython-36.pyc
byte-compiling /usr/local/lib/python3.6/dist-packages/krrt/__init__.py to __init__.cpython-36.pyc
running install_egg_info
Writing /usr/local/lib/python3.6/dist-packages/KR_Toolkit-0.1.egg-info
```

