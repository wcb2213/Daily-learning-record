#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/11


# 照这个思路太麻烦了啊
# t = 2
lInput1 = ['........', '........','........', '...*o...', '...o*...', '........', '........', '........']
n = 4
# lInput2 = [[3, 5, 0], [2, 5, 1], [2, 4, 0], [4, 5, 1]]
lInput2 = [[3, 5, 0]]
# process
lChess = []
for i in range(8):
    for j in range(8):
        if lInput1[i][j] == '*':
            lChess.append([i, j, 0])
        if lInput1[i][j] == 'o':
            lChess.append([i, j, 1])
# print(lChess)
def f1(l, dict={}):
    for i in range(len(l)):
        dict[(l[i][0], l[i][1])] = l[i][2]
    return dict
dict = f1(lChess)
# print(dict)

def f2(l):
    for i in range(len(l)):
        if l[i] == 0:
            return l.index(0)
    return 0
def f3(dict, l2):
    x, y, z = l2[0], l2[1], l2[2]
    if x != 0 and (x, y-1) in dict:
        l = []
        for i in range(y):
            if (x, i) in dict:
                l.append(dict[x, i]-z)
        l.reverse()
        for j in range(f2(l)):
            if z == 0:
                dict[x, y-1-j] = 0
                # dict[3, 4] = 0
            if z == 1:
                dict[x, y-1-j] = 1
    return dict

for i in range(1):
    dict = f3(dict, lInput2[i])
    dict = f1([lInput2[i]], dict)
print(dict)