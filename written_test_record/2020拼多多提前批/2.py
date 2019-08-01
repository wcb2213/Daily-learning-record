#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/28


# l1 = list(input().split(' '))

l1 = ['CAT', 'TIGER', 'RPC']
dict = {}
for i in l1:
    if i[0] not in dict:
        dict[i[0]] = 1
    else:
        dict[i[0]] += 1
    if i[-1] not in dict:
        dict[i[-1]] = 1
    else:
        dict[i[-1]] += 1
isTrue = True
for j in dict:
    if dict[j]%2==1:
        isTrue = False
        break
if isTrue:
    print("true")
else:
    print("false")