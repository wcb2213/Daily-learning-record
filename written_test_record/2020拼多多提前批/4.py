#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/28


# ac 5%
# n = int(input())
# li = list(map(int, input().split(' ')))
# wi = list(map(int, input().split(' ')))
n = 10
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
dict = {}
for i in range(len(li)):
    if li[i] not in dict:
        dict[li[i]]=wi[i]
    else:
        if dict[li[i]]>wi[i]:
            dict[li[i]] = wi[i]
# dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 10}
## 贪婪算法
li.sort(reverse=True)
weight = dict[li[0]]
totalweight = 0
count = 1
index = 1
while index<len(li):
    tmp = dict[li[index]]
    if totalweight+tmp <= weight*7:
        count += 1
        if tmp*8+totalweight<weight*7:
            weight = tmp
            totalweight = 0
        else:
            totalweight += tmp
    index += 1
print(count)