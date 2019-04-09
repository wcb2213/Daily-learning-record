#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/23


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)

if __name__ == '__main__':
    a = Solution()
    data = [1,2,2,3,3,3,4,4,4,5,5,5,5,5,5,5]
    l = list(map(str, data))
    print(a.GetNumberOfK(l, '5'))