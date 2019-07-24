#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


# 41ms
# 机器人的运动范围（反向考虑）
####  计数的回溯法
class Solution:
    def __init__(self):
        self.dict = {}

    def movingCount(self, threshold, rows, cols):
        # write code here
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        return self.recur(0, 0)

    def recur(self, i, j):
        if i >= self.rows or j >= self.cols or i < 0 or j < 0:
            return 0
        if sum(map(int, str(i)+str(j))) > self.threshold:
            return 0
        if (i, j) in self.dict:
            return 0
        self.dict[(i, j)] = 1
        return 1 + self.recur(i-1, j) + self.recur(i, j-1) + self.recur(i+1, j) + self.recur(i, j+1)
