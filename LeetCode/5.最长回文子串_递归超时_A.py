#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/10


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''

        def recursion1(i, j):
            if s[i] == s[j]:
                if j - i <= 1:
                    return True
                else:
                    return recursion1(i + 1, j - 1)
            else:
                return False

        n = len(s)
        strsub = ''
        lnum = 0
        for i in range(n):
            for j in range(i, n):
                if recursion1(i, j):
                    if j - i + 1 > lnum:
                        lnum = j - i + 1
                        strsub = s[i:j + 1]
        return strsub

if __name__ == '__main__':
    s = 'aacdefcaa'
    a = Solution()
    print(a.longestPalindrome(s))