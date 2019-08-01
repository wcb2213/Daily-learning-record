#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/22


# 正数划分问题 正整数分成若干整数的和

# 一.一般性，即对个数以及大小以及重复性不加约束
# dp(n,m)指 将正整数n划分后，每个正数都不大于m 的情况有几种
def dfs(n,m):
    if n==0 or m==0:
        return 0
    elif n<m:
        return dfs(n,n)
    elif n==m:
        return dfs(n,m-1)+1
    else:
        return dfs(n,m-1)+dfs(n-m,m)
# 边界条件：第一行及第一列全为0
# 转移方程：
# 当n<m：q(n,m)=q(n,n)
# 当n=m：q(n,m)=1+q(n,m-1)
# 当n>m: q(n,m)=q(n,m-1)+q(n-m,m) 没有m或至少一个m
n=m = 5
dp = [[0 for i in range(m+1)] for i in range(n+1)] # (n+1)*(m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        if i<j:
            dp[i][j] = dp[i][i]
        elif i==j:
            dp[i][j] = dp[i][j-1]+1
        else:
            dp[i][j] = dp[i][j-1]+dp[i-j][j]
print(dp[n][m])
print(dp)

# 二.对重复性有约束
# dp(n,m)指 将正整数n划分后，每个正数都不相同且不大于m 的情况有几种
def dfs(n,m):
    if n==0 or m==0:
        return 0
    elif n<m:
        return dfs(n,n)
    elif n==m:
        return dfs(n,m-1)+1
    else:
        return dfs(n,m-1)+dfs(n-m,m-1)
# 边界条件：第一行及第一列全为0
# 转移方程：
# 当n<m：q(n,m)=q(n,n) 同一
# 当n=m：q(n,m)=1+q(n,m-1) 同一
# 当n>m：q(n,m)=q(n,m-1)+q(n-m,m-1) 没有m或仅一个m
n=m = 5
dp = [[0 for i in range(m+1)] for i in range(n+1)] # (n+1)*(m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        if i<j:
            dp[i][j] = dp[i][i]
        elif i==j:
            dp[i][j] = dp[i][j-1]+1
        else:
            dp[i][j] = dp[i][j-1]+dp[i-j][j-1]
print(dp[n][m])
print(dp)

# 三.对元素的个数有约束。
# dp(n,k)指 将正整数n划分成k个正数相加的情况有几种
def dfs(n,k):
    if n<k:
        return 0
    elif n==k:
        return 1
    elif n>k:
        return dfs(n-k,k)+dfs(n-1,k-1)
# 边界条件：仅dp[0][0]为1 因为 n=m
# 转移方程：
# 当n<k：q(n,k)=0
# 当n=k：q(n,k)=1
# 当n>k：q(n,k)=q(n-k,k)+q(n-1,k-1) 每个整数都大于等于2或者至少有一个整数为1
n=k = 5
dp = [[0 for i in range(k+1)] for i in range(n+1)] # (n+1)*(k+1)
for i in range(n+1):
    for j in range(k+1):
        if i<j:
            dp[i][j] = 0
        elif i==j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-j][j]+dp[i-1][j-1]
print(dp[n][k])
print(dp)