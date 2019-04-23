#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/22

import pysnooper
# input
@pysnooper.snoop()
def f1(s):
    dict = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'SP':0,'BP':0}
    return dict[s]
l_input = list(map(f1, input().split(' ')))

# process
# 去除大小王
for i in range(len(l_input)):
    if l_input[i] == 0:
        l_input.pop(i)

# 如果l_input中最大值减去最小值的结果小于等于4 那么必能得到顺子
def f2(l):
    if max(l)-min(l) <= 4:
        return True
    else:
        return False
print(f2(l_input))