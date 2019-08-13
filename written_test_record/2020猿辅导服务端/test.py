#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/3


class Solution:
    def __init__(self):
        self.dict= {}
        self.flag = 1
    def main(self,n,m,k,M):
        self.n = n
        self.m = m
        self.M = M
        res = []
        for i in range(n):
            for j in range(m):
                self.dict = {}
                self.flag = 1
                self.dict[(i, j)] = 1
                self.search(k, i, j)
                res.append(self.flag)
        return res
    def search(self, k, i, j):
        if i<0 or j<0 or i>self.n-1 or j>self.m-1:
            return 0
        if M[i][j]
        return
n,m,k = 3,3,1
M = [[1, 3, 3], [2, 4, 9], [8, 9, 2]]
a = Solution()
print(max(a.main(n,m,k,M)))
