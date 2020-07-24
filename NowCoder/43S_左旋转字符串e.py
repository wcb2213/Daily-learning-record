#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/26


# 29ms
# 左旋转字符串
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or n < 0:
            return ''
        n = n % len(s)
        return s[n:] + s[:n]

if __name__ == '__main__':
    a = Solution()
    print(a.LeftRotateString('aaaabBB',4))