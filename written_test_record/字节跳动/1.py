#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/14


#### 扩散顺序是  当前 2 扩散 将 1 变成 2 新生成的 2 在扩散
####  这个递归是  一个 2 扩散到不能再扩散 下一个 2再扩散，不知道会不会影响
####  如果要改 怎么改

# input
l_input = []
for i in range(10):
    s = input().split()
    if s != []:
        l_input.append(s)

# process
# 递归处理
def recur(i, j):
    if i != 0 and l_input[i-1][j] == '1':
        l_input[i-1][j] = '2'
        res[i-1][j] = res[i][j]+1
        recur(i-1, j)
    if i != m-1 and l_input[i+1][j] == '1':
        l_input[i+1][j] = '2'
        res[i+1][j] = res[i][j]+1
        recur(i+1, j)
    if j != 0 and l_input[i][j-1] == '1':
        l_input[i][j-1] = '2'
        res[i][j-1] = res[i][j]+1
        recur(i, j-1)
    if j != n-1 and l_input[i][j+1] == '1':
        l_input[i][j+1] = '2'
        res[i][j+1] = res[i][j]+1
        recur(i, j+1)

m = len(l_input)
n = len(l_input[0])
res = [[0 for i in range(n)] for j in range(m)]
b = 0
for i in range(m):
    for j in range(n):
        if l_input[i][j] == '2':
            recur(i, j)
# output
for i in range(len(res)):
    if '1' in res[i]:
        b = 1
if b == 1:
    print(-1)
else:
    l_max = []
    for i in range(m):
        l_max.append(max(res[i]))
    print(max(l_max))