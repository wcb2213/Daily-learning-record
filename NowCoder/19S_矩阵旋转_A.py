#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/5


# matrix类型为二维列表，需要返回列表
#   1 分治
class Solution:
    def printMatrix(self, matrix):
        # write code here
        def trun(M):
            n, m = len(M), len(M[0])
            res = []
            for i in range(m - 1, -1, -1):
                tmp = []
                for j in range(n):
                    tmp.append(M[j][i])
                res.append(tmp)
            return res

        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix: return res
            matrix = trun(matrix)
#  2 直译
class Solution:
    def printMatrix(self, matrix):
        # write code here
        l,r,t,b,res=0,len(matrix[0])-1,0,len(matrix)-1,[]
        while True:
            for i in range(l,r+1): res.append(matrix[t][i])
            t+=1
            if t>b: break
            for i in range(t,b+1): res.append(matrix[i][r])
            r-=1
            if l>r: break
            for i in range(r,l-1,-1): res.append(matrix[b][i])
            b-=1
            if t>b: break
            for i in range(b,t-1,-1): res.append(matrix[i][l])
            l+=1
            if l>r: break
        return res