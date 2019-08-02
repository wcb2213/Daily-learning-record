#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


# 35ms
# 机器人的运动范围
####  计数的回溯法
class Solution:
    def __init__(self):
        self.flag = 0
        self.dict = {} ## 计数的回溯的dict要改成全局变量，以免多次计算
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.threshold = threshold
        self.rows = rows
        self.cols = cols
        if threshold < 0 or rows < 0 or cols < 0:
            return self.flag
        self.flag += 1
        self.dict[(0,0)] = 1
        self.search(0, 0)
        return self.flag
    def search(self, i, j):
        if i != 0 and (i-1, j) not in self.dict and self.block(i-1, j):
            self.flag += 1
            self.dict[(i-1,j)] =1
            self.search(i-1, j)
        if j != 0 and (i, j-1) not in self.dict and self.block(i, j-1):
            self.flag += 1
            self.dict[(i, j-1)]=1
            self.search(i, j-1)
        if i != self.rows-1 and (i+1, j) not in self.dict and self.block(i+1, j):
            self.flag += 1
            self.dict[(i+1, j)]=1
            self.search(i+1, j)
        if j != self.cols-1 and (i, j+1) not in self.dict and self.block(i, j+1):
            self.flag += 1
            self.dict[(i, j+1)]=1
            self.search(i, j+1)
        return
    def block(self, r, c):
        s = sum(map(int, str(r)+str(c)))
        return s <= self.threshold