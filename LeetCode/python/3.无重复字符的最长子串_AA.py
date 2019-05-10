#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/10


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        ans, j = 0, 0
        for i in range(len(s)):
            if s[i] in dict:
                # j 为子串的第一个字符的下标
                # 注意max 如 abba 轮到第二个a时  j不变
                j = max(j, dict[s[i]]+1)
            ans = max(ans, i-j+1)
            dict[s[i]] = i
        return ans