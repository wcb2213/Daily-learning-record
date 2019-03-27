#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/27


class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1
        res = list(range(n))
        i = 0
        while len(res) > 1:
            i = (m+i-1) % len(res) # 直接取余数 可保证 i 非负
            res.pop(i)
            # 下面这个不行，因为 i=i-1 可能为负数
            # i = (m + i) % len(res)
            # res.pop(i-1)
            # i = i - 1
        return res[0]


if __name__ == '__main__':
    a = Solution()
    n = 5
    m = 3
    print(a.LastRemaining_Solution(n, m))