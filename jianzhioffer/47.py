#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


# 加一个与算法判断 递归终止， 及 类的属性设置
class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        self.addSum(n)
        return self.sum
    def addSum(self, n):
        self.sum += n
        n -= 1
        return n>0 and self.addSum(n)

if __name__ == '__main__':
    a = Solution()
    n = 5
    print(a.Sum_Solution(n))