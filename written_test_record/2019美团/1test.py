#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/23


n,m=3,3
l=[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
l1,l2=[],[] # l1 偶数项 l2 奇数项
for i in range(n):
    for j in range(m):
        if (i+j)%2 == 0:
            l1.append(l[i][j])
        else:
            l2.append(l[i][j])

def max_list(l):
    res = []
    for i in l:
        res.append(l.count(i))
    return res
w1 = max_list(l1)
w11 = sorted(list(set(w1)))
w11 = [0]*(len(w1)-len(w11)) +w11
n1 = l1[w1.index(w11[-1])]
w2 = max_list(l2)
w22 = sorted(list(set(w2)))
w22 = [0] * (len(w2) - len(w22)) + w22
n2 = l2[w2.index(w22[-1])]
if n1 != n2:
    print(len(l1)-w11[-1]+len(l2)-w22[-1])
else:
    print(min(len(l1)-w11[-2]+len(l2)-w22[-1],len(l1)-w11[-1]+len(l2)-w22[-2]))