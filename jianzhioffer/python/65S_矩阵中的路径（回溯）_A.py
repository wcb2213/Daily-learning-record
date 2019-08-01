#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


# 30ms
# 矩阵中的路径
####  不计数的回溯法 注意 dict不能设置为全局变量，这样才能在各个情况之间回溯
class Solution:
    def __init__(self):
        self.isTrue = False
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        self.matrix = [matrix[r*cols:(r+1)*cols] for r in range(rows)]
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j] == path[0]:
                    self.search(path[1:], [(i, j)], i, j)
                    if self.isTrue:
                        return True
        return False
    def search(self, path, dict, i, j):
        if path == '':
            self.isTrue = True
            return
        if i != 0 and (i - 1, j) not in dict and self.matrix[i - 1][j] == path[0]:
            self.search(path[1:], dict + [(i - 1, j)], i - 1, j)
        if i != self.rows - 1 and (i + 1, j) not in dict and self.matrix[i + 1][j] == path[0]:
            self.search(path[1:], dict + [(i + 1, j)], i + 1, j)
        if j != 0 and (i, j - 1) not in dict and self.matrix[i][j - 1] == path[0]:
            self.search(path[1:], dict + [(i, j - 1)], i, j - 1)
        if j != self.cols - 1 and (i, j + 1) not in dict and self.matrix[i][j + 1] == path[0]:
            self.search(path[1:], dict + [(i, j + 1)], i, j + 1)
        return