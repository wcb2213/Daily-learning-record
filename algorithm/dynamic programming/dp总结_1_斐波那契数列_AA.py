#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/20


# ①自顶向下的备忘录法 还是用了递归
# def f(n):
#     if n==1 or n==2:
#         return 1
#     if dp[n-1] == 0:
#         dp[n-1] = f(n-1)
#     if dp[n-2] == 0:
#         dp[n-2] = f(n-2)
#     return dp[n-1]+dp[n-2]
# n = 5
# dp=[0]*(n+1) ## 辅助存储，避免多次计算
print(list(map(f, range(1,n+1))))


# ②自底向上的动态规划  推荐
def f2(n):
    # write code here
    l = [0,1,1]
    for i in range(3,n+1):
        l.append(l[i-2]+l[i-1])
    return l[n]