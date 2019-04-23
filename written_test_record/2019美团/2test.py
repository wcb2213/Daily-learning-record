#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/23


n = 3
l = [[1, 2, 3, 2], [2, 5, 2, 3], [1, 4, 3, 4]]

l1, l2 = [], [] #l1 x； l2 y
for i in range(n):
    l1.append(l[i][0])
    l1.append(l[i][2])
    l2.append(l[i][1])
    l2.append(l[i][3])
xmin = min(l1)
xmax = max(l1)
ymin = min(l2)
ymax = max(l2)
r = xmax-xmin+1
c = ymax-ymin+1
dp = [[0 for i in range(c)] for j in range(r)] #r * c
# print(dp)

def f1(a,b,r): #抹黑一行
    nmin = min(a,b)
    for i in range(abs(b-a)+1):
        dp[r-xmin][i+nmin-ymin] = 1
def f2(a,b,c): #抹黑一列
    nmin = min(a,b)
    for i in range(abs(b-a)+1):
        dp[i+nmin-xmin][c-ymin] = 1
for i in range(n):
    if l[i][0] == l[i][2]:
        f1(l[i][1], l[i][3], l[i][0])
    else:
        f2(l[i][0], l[i][2], l[i][1])
# print(dp)
flag = 0
for i in range(r):
    for j in range(c):
        if dp[i][j] == 1:
            flag += 1
print(flag)