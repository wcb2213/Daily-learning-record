#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


class Solution:
    def __init__(self):
        self.dict = {}

    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.recur(threshold, rows, cols, 0, 0)

    def recur(self, k, r, c, i, j):
        if i/10 + i%10 + j/10 + j%10 > k:
            return 0
        if i >= r or j >= c or i < 0 or j < 0:
            return 0
        if (i, j) in self.dict:
            return 0
        self.dict[(i, j)] = 1
        return 1 + self.recur(k, r, c, i-1, j) + self.recur(k, r, c, i, j-1) + self.recur(k, r, c, i+1, j) + self.recur(k, r, c, i, j+1)