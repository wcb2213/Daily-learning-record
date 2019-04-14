#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/14


# input
l_input = []
for i in range(10):
    s = input().split()
    if s != []:
        l_input.append(s)
# print(l_input)
l_input = [['1', '2'], ['2', '1'], ['1', '2'], ['0', '1'], ['0', '1'], ['1', '1']]

# process
def recur(i, j):
    if i != 0 and l_input[i-1][j] == '1':
        l_input[i-1][j] == '2'
        res[i-1][j] = res[i][j]+1
        recur(i-1, j)
    if i != m-1 and l_input[i+1][j] == '1':
        l_input[i+1][j] == '2'
        res[i+1][j] = res[i][j]+1
        recur(i+1, j)
    if j != 0 and l_input[i][j-1] == '1':
        l_input[i][j-1] == '2'
        res[i][j-1] = res[i][j]+1
        recur(i, j-1)
    if j != n-1 and l_input[i][j+1] == '1':
        l_input[i][j+1] == '2'
        res[i][j+1] = res[i][j]+1
        recur(i, j+1)

m = len(l_input)
n = len(l_input[0])
res = [[0 for i in range(n)] for j in range(m)]
b = 0

l_two = []
for i in range(m):
    for j in range(n):
        if l_input[i][j] == '2':
            l_two.append([i,j])
for i in range(len(l_two)):
    recur(l_two[i][0], l_two[i][1])

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