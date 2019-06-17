#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/22


# 找到list中含有最大和的连续子序列
def max_subarry(l):
    if max(l) < 0:
        return [max(l)]
    # 1. 求出最大和
    pre = l[0]
    res = [l[0]]
    for i in range(1,len(l)):
        if pre >= 0:
            pre = pre+l[i]
            res.append(pre)
        else:
            pre = l[i]
            res.append(pre)
    # print(res)
    num_max_subarry = max(res)

    # 2.找出该子序列
    idx2 = res.index(num_max_subarry)
    for i in range(idx2-1, -1, -1):
        if res[i] < 0:
            idx1 = i+1
            break
    return l[idx1:idx2+1], num_max_subarry


l = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarry(l))