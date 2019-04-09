#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


from functools import reduce
class Solution:
    def __init__(self):
        self.digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        a = ''
        if s[0] == '+' or s[0] == '-':
            a = s[0]
            s = s[1:]
        if not s:
            return 0
        for i in s:
            if i not in self.digits:
                return 0
        if a == '-':
            return 0 - self.str2int(s)
        else:
            return self.str2int(s)

    def str2int(self, s):
        def char2num(s):
            return self.digits[s]
        def fn(x, y):
            return x * 10 + y
        def str2int(s):
            return reduce(fn, map(char2num, s))
        return str2int(s)

if __name__ == '__main__':
    a = Solution()
    s = '-2147483647'
    print(a.StrToInt(s))