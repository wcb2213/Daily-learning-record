#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/22


# 正数划分问题 正整数n
# dfs（n,m）指 将正整数n划分后，每个正数都不大于m 的情况有几种

# #### 1 递归
# def dfs(n,m):
#     if n==1 or m==1:
#         return 1
#     elif n<m:
#         return dfs(n,n)
#     elif n==m:
#         return dfs(n,m-1)+1
#     else:
#         return dfs(n,m-1)+dfs(n-m,m) # 没有m及至少有一个m
# n=m = 5
# print(dfs(n,m))


#### 3 自底向上 动态规划
def dfs(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i<j:
                dp[i][j] = dp[i][i]
            elif i==j:
                dp[i][j] = dp[i][j-1]+1
            else:
                dp[i][j] = dp[i][j-1]+dp[i-j][j]
n=m = 5
dp = [[0 for i in range(m+1)] for i in range(n+1)] # n*m
dfs(n,m)
print(dp)
