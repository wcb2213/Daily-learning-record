#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/20


# ①自顶向下的备忘录法 还是用了递归
# class Solution:
#     def __init__(self):
#         self.l = [0,1]+[-1]*38
#     def Fibonacci(self, n):
#         # write code here
#         if n<=1: return n
#         if self.l[n-1]==-1:
#             self.l[n-1]=self.Fibonacci(n-1)
#         if self.l[n-2]==-1:
#             self.l[n-2]=self.Fibonacci(n-2)
#         return self.l[n-1]+self.l[n-2]


# ②自底向上的动态规划  推荐on+on
def f2(n):
    # write code here
    l = [0,1]
    for i in range(2,n+1):
        l.append(l[i-2]+l[i-1])
    return l[n]

# 3优化  on+o1
def f3(n):
    if n<=1: return n
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b
