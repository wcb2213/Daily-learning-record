#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


# 23ms
# 输入n个整数，找出其中最小的K个数。
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        tinput = sorted(tinput)
        return tinput[0:k]

if __name__ == '__main__':
    a = Solution()
    l = [4,5,1,6,2,7,3,8]
    print(a.GetLeastNumbers_Solution(l, 4))
