#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/11


n = 4
list = [3, 9, 2, 7]

dp = [100]*n
def f(index):
    dp[index-1]+=100
    if index-1==0 or list[index-2]<list[index-1]:
        return
    if list[index-1]==list[index-2]:
        return f(index-1)
    if list[index-2]>list[index-1]:
        if dp[index-2]==dp[index-1]:
            return f(index-1)
        return
for i in range(1,n):
    if list[i]<list[i-1]:
        if dp[i-1]==100:
            f(i)
            dp[i]=100
        else:
            dp[i]=100
    elif list[i]==list[i-1]: dp[i]=dp[i-1]
    elif list[i]>list[i-1]:dp[i]=dp[i-1]+100

print(sum(dp))