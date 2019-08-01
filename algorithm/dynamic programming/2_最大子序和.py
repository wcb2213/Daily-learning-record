#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/22


# 找到list中含有最大和的连续子序列
def max_sublist(l):
    if max(l) < 0:
        return [max(l)], max(l)
    # 1. 求出最大和
    pre = l[0]
    res = [l[0]]  ## 从下往上考虑
    for i in range(1,len(l)):
        if pre >= 0:  ## 取得最大和的子序列会更长
            pre = pre+l[i]
            res.append(pre)
        else:
            pre = l[i]
            res.append(pre)
    # print(res)
    num_max_sublists = max(res)

    # 2.找出该子序列
    idx2 = res.index(num_max_sublists)
    for i in range(idx2-1, -1, -1): # range(start, stop[, step])
        if res[i] < 0:
            idx1 = i+1
            break
    return l[idx1:idx2+1], num_max_sublists


l = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sublist(l))