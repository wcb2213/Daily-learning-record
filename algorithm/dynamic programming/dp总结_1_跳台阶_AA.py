#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/20


# ①自顶向下的备忘录法 还是用了递归
# def f(n):
#     if n<=2:
#         return n
#     if dp[n-1] == 0:
#         dp[n-1] = f(n-1)
#     if dp[n-2] == 0:
#         dp[n-2] = f(n-2)
#     return dp[n-1]+dp[n-2]
# dp=[0]*5
# print(f(5))
# print(dp)

# ②自底向上的动态规划  没用递归 比上面好点
### 能用这个最好
def f2(n):
    # write code here
    f1, f2 = 1, 2
    if n<=2:
        return n
    for i in range(3, n + 1):
        a = f1 + f2
        f1, f2 = f2, a
    return a
print(list(map(f2, list(range(1,5))))) ## 也可保存在一个链表中