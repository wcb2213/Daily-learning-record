#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/23


# 37ms
# 统计一个数字在排序数组中出现的次数。
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)

if __name__ == '__main__':
    a = Solution()
    data = [1,2,2,3,3,3,4,4,4,5,5,5,5,5,5,5]
    l = list(map(str, data))
    print(a.GetNumberOfK(l, '5'))