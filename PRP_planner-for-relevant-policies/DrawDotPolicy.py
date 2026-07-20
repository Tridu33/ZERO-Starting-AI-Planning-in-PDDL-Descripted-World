#!/usr/bin/env python 
# -*- coding:UTF-8 -*-
# 
"""
Draw dot for policy
"""
import re
import os,sys

def create_dir_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)
def main(domainname):
    create_dir_not_exist(os.path.join(os.getcwd(),"solutionsByPRP"))        
    sub_fond_dot = "solutionsByPRP/fond_{0}.dot".format(domainname) 
    sub_fond_png = "solutionsByPRP/fond_{0}.png".format(domainname)
    sub_fond_dot = os.path.join(os.getcwd(),sub_fond_dot)
    sub_fond_png = os.path.join(os.getcwd(),sub_fond_png)
    RUN_CMD_For_Dot  = "dot -Tpng {0} -o {1}".format(sub_fond_dot,sub_fond_png)
    sub_fond_dot_str = "digraph G {\n    node [shape=plaintext]"
    
    pattern = re.compile(r'Execute: ([^\s]+)  /')
    with  open  (os.path.join(os.getcwd(),"solutionsByPRP/fond_{0}_human_policy.out".format(domainname)) ,  "r")  as  myfile:
        for  line in  myfile:
            line = line.replace('virtual_source_act','virtualSourceAct')
            action_name_list = pattern.findall(line)
            if len(action_name_list) == 1:
                action_name = action_name_list[0]
                temp_list_actionname = action_name.split('_')
                if len(temp_list_actionname) == 3:
                    sub_fond_dot_str += '\n'+temp_list_actionname[0] + '->' + temp_list_actionname[2] + '[label = "{0}"]'.format(temp_list_actionname[1])
                else:
                    targets = temp_list_actionname[2:]
                    for each_target in targets:
                        sub_fond_dot_str += '\n'+temp_list_actionname[0] + '->' + each_target + '[label = "{0}"]'.format(temp_list_actionname[1])
                sub_fond_dot_str += '\n'
    sub_fond_dot_str += '\n}'
    with open(sub_fond_dot, 'w+', encoding='utf-8') as f:
        f.write(sub_fond_dot_str)
    os.system(RUN_CMD_For_Dot)
    
if __name__ == '__main__':
    import argparse
    args_parser = argparse.ArgumentParser(description='Graph for Policy autoGenerator')
    args_parser.add_argument('-domainname', default = "blocks_clear", help='Path to fond domain files(default=dfs). -- OPTIONAL')
    params = vars(args_parser.parse_args())
    domainname = params['domainname']
    main(domainname)








