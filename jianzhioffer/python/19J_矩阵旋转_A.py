#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


# 24ms
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):# matrix 为二维list
        # write code here
        res = []
        while matrix:
            res += matrix.pop(0)
            # res.append(matrix.pop(0)) ## 不行 res为一维list
            if not matrix:
                break
            matrix = self.turn(matrix)
        return res
    def turn(self, M): # 矩阵逆时针旋转
        m = len(M)
        n = len(M[0])
        res = []
        for i in range(n):
            l = []
            for j in range(m):
                l.append(M[j][n-i-1])
            res.append(l)
        return res