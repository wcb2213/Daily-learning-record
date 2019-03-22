#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/22


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        l = list(s)
        weightL = self.weightList(l)
        for i in range(len(weightL)):
            if weightL[i] == 1:
                return i
        return -1

    def weightList(self, L):
        res = []
        n = len(L)
        for i in range(n):
            num = 0
            for j in range(n):
                if L[j] == L[i]:
                    num += 1
            res.append(num)
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.FirstNotRepeatingChar('aaaabBB'))