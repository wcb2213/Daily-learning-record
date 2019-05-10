#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


# 35ms

class Solution:
    def __init__(self):
        self.flag = 1
        self.dict = [(0,0)]
    def movingCount(self, threshold, rows, cols):
        # write code here
        # dict 改成全局变量
        def search(i, j):
            if i != 0 and not (i-1, j) in self.dict and block(i-1, j):
                self.flag += 1
                self.dict += [(i-1, j)]
                search(i-1, j)
            if j != 0 and not (i, j-1) in self.dict and block(i, j-1):
                self.flag += 1
                self.dict += [(i, j-1)]
                search(i, j-1)
            if i != rows-1 and not (i+1, j) in self.dict and block(i+1, j):
                self.flag += 1
                self.dict += [(i+1, j)]
                search(i+1, j)
            if j != cols-1 and not (i, j+1) in self.dict and block(i, j+1):
                self.flag += 1
                self.dict += [(i, j+1)]
                search(i, j+1)

        def block(r, c):
            s = sum(map(int, str(r)+str(c)))
            return s <= threshold

        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        search(0, 0)
        return self.flag