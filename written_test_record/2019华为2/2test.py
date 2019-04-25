#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/24


n,m=4,5
l = [[1, 2, 3], [1, 3, 3], [1, 4, 4], [2, 3, 5], [3, 4, 3]]
des = [1, 3]

l1,l2 = [],[]
n = []
for i in range(m):
    if l[i][0] == des[0]:
        if l[i][1] == des[1]:
            n.append(l[i][2])
        else:
            l1.append([l[i][1],l[i][2]])
    if l[i][1] == des[1]:
        if l[i][0] != des[0]:
            l2.append([l[i][0],l[i][2]])
# print(n,l1,l2)

n1 = len(l1)
n2 = len(l2)
for i in range(n1):
    for j in range(n2):
        if l1[i][0] == l2[j][0]:
            n.append(l1[i][1]+l2[j][0]-1)
# print(n)
print(min(n))
