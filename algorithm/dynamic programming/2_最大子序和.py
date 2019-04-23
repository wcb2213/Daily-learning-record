#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/22


# 找到list中含有最大和的连续子序列
def max_subarry(l):
    if max(l) < 0:
        return [max(l)]
    pre = l[0]
    res = [l[0]]
    for i in range(1,len(l)):
        if pre >= 0:
            pre = pre+l[i]
            res.append(pre)
        else:
            pre = l[i]
            res.append(pre)

    idx2 = res.index(max(res))
    for i in range(idx2):
        if res[idx2-1-i] < 0:
            idx1 = idx2-1-i
            break
    return l[idx1+1:idx2+1], sum(l[idx1+1:idx2+1])


l = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarry(l))