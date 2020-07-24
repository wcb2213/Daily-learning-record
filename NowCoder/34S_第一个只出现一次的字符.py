#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/22


# 第一个只出现一次的字符
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic={}
        for c in s:
            dic[c]= not (c in dic)
        for i in range(len(s)):
            if dic[s[i]]:
                return i
        # python 3.6以后 字典有序
        # for k,v in dic.items():
        #     if v:
        #         return k
        return -1


if __name__ == '__main__':
    a = Solution()
    print(a.FirstNotRepeatingChar('aaaabBB'))