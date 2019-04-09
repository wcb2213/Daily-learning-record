#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/26


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or n < 0:
            return ''
        l = list(s)
        n = n%(len(l))
        for i in range(n):
            a = l.pop(0)
            l.append(a)
        return ''.join(l)

if __name__ == '__main__':
    a = Solution()
    print(a.LeftRotateString('aaaabBB',4))