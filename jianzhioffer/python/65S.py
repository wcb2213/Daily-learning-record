#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


class Solution:
    # 输入的matrix是一个字符串
    def hasPath(self, matrix, rows, cols, path):
        self.cols, self.rows = cols, rows
        matrix = [matrix[r * cols:(r + 1) * cols] for r in range(0, rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    self.b = False
                    self.search(matrix, path[1:], [(i, j)], i, j)
                    if self.b:
                        return True
        return False

    # s = 'abc'
    # print(s[3:] == '')
    # True
    # l = [1, 2, 3]
    # print(l[3:] == [])
    # True
    def search(self, matrix, path, dict, i, j):
        if path == "":
            self.b = True
            return
        if j != 0 and (i, j - 1) not in dict and matrix[i][j - 1] == path[0]:
            self.search(matrix, path[1:], dict + [(i, j - 1)], i, j - 1)
        if i != 0 and (i - 1, j) not in dict and matrix[i - 1][j] == path[0]:
            self.search(matrix, path[1:], dict + [(i - 1, j)], i - 1, j)
        if j != self.cols - 1 and (i, j + 1) not in dict and matrix[i][j + 1] == path[0]:
            self.search(matrix, path[1:], dict + [(i, j + 1)], i, j + 1)
        if i != self.rows - 1 and (i + 1, j) not in dict and matrix[i + 1][j] == path[0]:
            self.search(matrix, path[1:], dict + [(i + 1, j)], i + 1, j)