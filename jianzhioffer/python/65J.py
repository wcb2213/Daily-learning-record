#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


# -*- coding:utf-8 -*-
class FoundExp(Exception): pass
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        def traverse(r, c, i, acc):
            if i==len(path): raise FoundExp()
            if not (0<=r<rows and 0<=c<cols): return
            if (r,c) in acc: return
            if matrix[r*cols+c]!=path[i]: return
            acc.add((r,c))
            traverse(r-1,c,i+1,acc)
            traverse(r+1,c,i+1,acc)
            traverse(r,c-1,i+1,acc)
            traverse(r,c+1,i+1,acc)
            acc.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                try:
                    traverse(r,c,0,set())
                except FoundExp:
                    return True
        return False