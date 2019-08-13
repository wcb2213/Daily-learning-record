#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/11


n,k = map(int,input().split(' '))
s = list(map(int,list(input())))

dp = [0]*(n+k-1)
def countOne(list):
    return list.count(1)%2==0
for i in range(k-1,n+k-1):
    if countOne(dp[i-k+1:i]+[s[i-k+1]]):
        dp[i]=0
    else:
        dp[i]=1
res = dp[k-1:]
print(''.join(map(str,res)))