#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/26


24ms
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            a=1
            for j in range(i):
                a *=A[j]
            B.append(a)
        for i in range(len(A)-1):
            a=1
            for j in range(i+1,len(A)):
                a *=A[j]
            B[i] *= a
        return B