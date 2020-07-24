#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/26


# 26ms
# 翻转单词顺序列 牛客的示例真的啥笔
class Solution:
    def ReverseSentence(self, s):
        return ' '.join(s.split(' ')[::-1])


if __name__ == '__main__':
    a = Solution()
    print(a.ReverseSentence('student. a am I'))