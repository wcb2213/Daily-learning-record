#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/17

import sys

n = int(sys.stdin.readline())
L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))

## weightList
## 如 [1,2,3,4,5,5,5,6,6] 权重值数组为[1,1,1,1,3,3,3,2,2]
def weightList():
    res = []
    for i in range(n):
        num = 0
        for j in range(n):
            if L1[j] == L1[i]:
                num += 1
        res.append(num)
    return res

# needcutNum int 需要调整的椅子腿数量
# weight list 权重系数最大值的权重值,可能有多个值
def count(needcutNum, weight):
    # 每个重数情况下调整椅子腿所需的最小能量
    res = []
    # 遍历所有权重值
    while weight:
        w = weight.pop()
        # l4为L2除权重值对应元素之外的元素
        l4 = []
        for i in range(n):
            if L1[i] != w:
                l4.append(L2[i])
        # minNum 保存l4中能量最小的 needcutNum 个元素
        minNum = []
        sortl4 = sorted(l4, reverse=True)
        for i in range(needcutNum):
            minNum.append(sortl4.pop(0))

        res.append(sum(minNum))
    return res

# 权重数列
l3 = weightList()

# weight_num 权重系数最大值
weight_num = max(l3)

# weight 权重系数最大值的权重值,可能有多个值
weight = []
for i in range(n):
    if l3[i] == weight_num:
        weight.append(L1[i])
weight = list(set(weight))
# print(weight)

# needNum 保持桌子稳定的最小椅子腿数量
needNum = int(n/2+1)

# 输出调整桌腿的最小能量
if weight_num >= needNum:
    print(0)
else:
    needcutNum = needNum - weight_num
    res = count(needcutNum, weight)
    print(min(res))







