#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/26


class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ''
        l = list(s.split(' '))
        res = []
        for i in range(len(l)):
            res.append(l.pop())
        return ' '.join(res)


if __name__ == '__main__':
    a = Solution()
    print(a.ReverseSentence('student. a am I'))