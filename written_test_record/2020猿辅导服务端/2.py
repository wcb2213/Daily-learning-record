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
        if i!=0 and (i-1,j) not in self.dict and (k>0 or self.M[i-1][j]>self.M[i][j]):
            self.flag += 1
            self.dict[(i-1,j)]=1
            if self.M[i-1][j]<=self.M[i][j]:
                k -= 1
            self.search(k,i-1,j)
        if i!=self.n-1 and (i+1,j) not in self.dict and (k>0 or self.M[i+1][j]>self.M[i][j]):
            self.flag += 1
            self.dict[(i+1,j)]=1
            if self.M[i+1][j]<=self.M[i][j]:
                k -= 1
            self.search(k,i+1,j)
        if j!=0 and (i,j-1) not in self.dict and (k>0 or self.M[i][j-1]>self.M[i][j]):
            self.flag += 1
            self.dict[(i,j-1)]=1
            if self.M[i][j-1]<=self.M[i][j]:
                k -= 1
            self.search(k,i,j-1)
        if j!=self.m-1 and (i,j+1) not in self.dict and (k>0 or self.M[i][j+1]>self.M[i][j]):
            self.flag += 1
            self.dict[(i,j+1)]=1
            if self.M[i][j+1]<=self.M[i][j]:
                k -= 1
            self.search(k,i,j+1)
        return
# n,m,k = map(int, input().split(' '))
# M = []
# for i in range(n):
#     M.append(list(map(int, input().split(' '))))

n,m,k = 3,3,1
M = [[1, 3, 3], [2, 4, 9], [8, 9, 2]]
a = Solution()
print(max(a.main(n,m,k,M)))

