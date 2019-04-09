#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            # res.append(matrix.pop(0)) ##语法应该没错  也许2.7不行？
            if not matrix:
                break
            matrix = self.turn(matrix)
        return res
    def turn(self, M):
        n = len(M)
        m = len(M[0])
        res = []
        for i in range(m):
            l = []
            for j in range(n):
                l.append(M[j][i])
            res.append(l)
        res.reverse()
        return res
