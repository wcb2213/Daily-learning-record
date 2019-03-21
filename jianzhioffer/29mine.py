#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        res = []
        if k > len(tinput):
            return []
        for i in range(k):
            res.append(min(tinput))
            tinput.pop(tinput.index(min(tinput)))
        return res

if __name__ == '__main__':
    a = Solution()
    l = [4,5,1,6,2,7,3,8]
    print(a.GetLeastNumbers_Solution(l, 4))
