#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/2


#前i个数中子数组和为j的方法数
l = [0,5,10,15,20,30]
target = 50
dp = [[0 for _ in range(target+1)] for _ in range(len(l))]
for i in range(1,len(l)):
    for j in range(1,target+1):
        if l[i]>target:
            dp[i][j] = dp[i-1][j]
        elif l[i]==j:
            dp[i][j] = dp[i-1][j]+1
        else:
            dp[i][j] = dp[i-1][j]+dp[i-1][j-l[i]]
print(dp)