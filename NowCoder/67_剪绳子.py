#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/13


class Solution:
    def cutRope(self, number):
        n=number
        if n==2: return 1
        if n==3: return 2
        if n==4: return 4
        k=n//3
        if n-3*k==0: return 3**k
        elif n-3*k==1: return 3**(k-1)*4
        else: return 3**k*2

    # def cutRope(self, number):
    #     # write code here
    #     n=number
    #     if n==2: return 1
    #     if n==3: return 2
    #     dp=[0]*(n+1)
    #     dp[1],dp[2],dp[3]=1,2,3
    #     for i in range(4,n+1):
    #         for j in range(1,i//2+1):
    #             dp[i]=max(dp[i],dp[j]*dp[i-j])
    #     return dp[n]