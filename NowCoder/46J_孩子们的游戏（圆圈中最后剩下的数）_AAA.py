#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/27


# 29ms
# 孩子们的游戏（圆圈中最后剩下的数）
# 环形链表
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n==0: return -1
        i=0
        l=list(range(n))
        while len(l)>1:
            i=(i+m-1)%len(l)
            l.pop(i)
        return l[0]


if __name__ == '__main__':
    a = Solution()
    n = 5
    m = 3
    print(a.LastRemaining_Solution(n, m))