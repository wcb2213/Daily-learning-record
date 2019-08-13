#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/3


# n,k= map(int,input().split(' '))
n,k=4,3

dp = [[0 for _ in range(2+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,3):
        dp[i][1] = dp[i - 1][2]
        dp[i][2] = (k - 1) ** i - dp[i][1]
print(dp[n][1]%1000000007)