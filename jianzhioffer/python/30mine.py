#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        n = len(array)
        if n<1:
            return []
        res = []
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += array[j]
                res.append(sum)
        return max(res)

if __name__ == '__main__':
    a = Solution()
    l = [1,-2,3,10,-4,7,2,-5]
    print(a.FindGreatestSumOfSubArray(l))
