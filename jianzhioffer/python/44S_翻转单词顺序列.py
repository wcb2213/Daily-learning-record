#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/26


# 26ms
# 翻转单词顺序列
class Solution:
    def ReverseSentence(self, s):
        if not s:
            return ''
        l = list(s.split(' '))
        l.reverse()
        return ' '.join(map(str,l))


if __name__ == '__main__':
    a = Solution()
    print(a.ReverseSentence('student. a am I'))