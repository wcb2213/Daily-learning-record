#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/25


# 27ms
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                break
        return i

if __name__ == '__main__':
    a = Solution()
    print(a.FirstNotRepeatingChar('aaaabBB'))