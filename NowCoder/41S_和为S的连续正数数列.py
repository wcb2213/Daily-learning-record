#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/25


# 和为S的连续正数数列
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        def sum_a2b(a,b):
            return (a+b)*(b-a+1)/2
        i,j,sum=1,1,0
        res=[]
        while i<=tsum//2:
            if sum_a2b(i, j-1)>tsum:
                i+=1
            elif sum_a2b(i, j-1)<tsum:
                j+=1
            else:
                res.append(list(range(i,j)))
                i+=1
        return res
