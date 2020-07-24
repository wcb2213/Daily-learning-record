#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/5


class Solution:
    # matrix类型为二维列表，需要返回列表
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