#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
class Solution:
    def Sum_Solution(self, n):
        # write code here
        l = list(range(1, n+1))
        return sum(l)


if __name__ == '__main__':
    a = Solution()
    n = 5
    print(a.Sum_Solution(n))