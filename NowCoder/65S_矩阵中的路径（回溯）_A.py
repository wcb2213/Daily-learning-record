#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


# 30ms
# 矩阵中的路径
# 严格来讲，并没有回溯的过程
class Solution:
    def __init__(self):
        self.isTrue = False
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        matrix = [matrix[r*cols:(r+1)*cols] for r in range(rows)]
        
        def search(index, visited, i, j):
            if index==len(path):
                self.isTrue=True
                return
            if not (0<=i<rows and 0<=j<cols): return
            if (i,j) in visited: return
            if matrix[i][j]!=path[index]: return
            visited.add((i,j))
            search(index + 1, visited, i-1, j)
            search(index + 1, visited, i+1, j)
            search(index + 1, visited, i, j-1)
            search(index + 1, visited, i, j+1)

        for i in range(rows):
            for j in range(cols):
                search(0, set(), i, j)
                if self.isTrue:
                    return True
        return False