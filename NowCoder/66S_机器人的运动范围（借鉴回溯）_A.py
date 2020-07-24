#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


# 35ms
# 机器人的运动范围
# 形式跟回溯很像，但并不是回溯
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def block(r, c):
            s = sum(map(int, str(r) + str(c)))
            return s <= threshold

        def search(visited, i, j):
            if not (0<=i<rows and 0<=j<cols): return
            if (i,j) in visited: return
            if block(i,j):
                self.flag+=1
                visited.add((i, j))
                search(visited, i+1, j)
                search(visited, i-1, j)
                search(visited, i, j+1)
                search(visited, i, j-1)


        self.flag = 0
        if threshold < 0 or rows < 0 or cols < 0:
            return self.flag

        search(set(),0, 0)
        return self.flag