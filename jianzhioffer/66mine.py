#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


class Solution:
    def __init__(self):
        self.flag = 1
    def movingCount(self, threshold, rows, cols):
        # write code here
        # 计数不对
        def search(dict, i, j):
            if i != 0 and not (i-1, j) in dict and block(i-1, j):
                self.flag += 1
                search(dict+[(i-1, j)], i-1, j)
            if j != 0 and not (i, j-1) in dict and block(i, j-1):
                self.flag += 1
                search(dict+[(i, j-1)], i, j-1)
            if i != rows-1 and not (i+1, j) in dict and block(i+1, j):
                self.flag += 1
                search(dict+[(i+1, j)], i+1, j)
            if j != cols-1 and not (i, j+1) in dict and block(i, j+1):
                self.flag += 1
                search(dict+[(i, j+1)], i, j+1)

        def block(r, c):
            s = sum(map(int, str(r)+str(c)))
            return s <= threshold

        if threshold < 0 or rows < 0 or cols < 0:
            return None
        search([(0, 0)], 0, 0)
        return self.flag


if __name__ == '__main__':
    a = Solution()
    print(a.movingCount(5,10,10))