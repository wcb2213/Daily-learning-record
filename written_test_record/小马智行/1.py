#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/21


# input
n, h = map(int, input().split(' '))
l_input = list(map(int, input().split(' ')))

# process
l_tan =[]
for i in range(n):
    l_tan.append((h-l_input[i])/(i+1))

# output
output = [0]*n
for i in range(1,n):
    for j in range(0,i):
        if l_tan[i] >= l_tan[i-1-j]:
            output[i] = i-j
            break
for i in output:
    print(i)