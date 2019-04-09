#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/27


## 复杂度高了，没搞懂是哪个的问题
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n or not m:
            return -1
        l = [i for i in range(n)]
        for i in range(n-1):# 抛出n-1个熊孩子，舒服
            if m > n:
                m_remainder = m % (len(l))
            else:
                m_remainder = m
            for j in range(m_remainder-1):
                # l.append(l.pop(j))# pop 当前数组
                l.append(l.pop(0))
            l.pop(0)
        return l[0]

if __name__ == '__main__':
    a = Solution()
    n = 5
    m = 3
    print(a.LastRemaining_Solution(n, m))