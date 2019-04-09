#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        k = self.weightList(numbers)
        n = len(numbers)
        for i in range(n):
            if k[i] > n/2:
                return numbers[i]
        return 0

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
    l = [1,2,3,2,2,2,5,4,2]
    print(a.weightList(l))
    print(a.MoreThanHalfNum_Solution(l))
