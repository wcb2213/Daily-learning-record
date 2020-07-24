#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/23


# 37ms
# 统计一个数字在排序数组中出现的次数。
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or data[0]>k or data[-1]<k: return 0

        l, r = 0, len(data) - 1
        if data[0]==k: lb=-1
        else:
            while l+1<r:
                mid = (l+r)//2
                if data[mid]<k: l=mid
                elif data[mid]>=k: r=mid
            lb=l

        r=len(data)-1
        if data[r]==k: rb=r+1
        else:
            while l+1<r:
                mid = (l+r)//2
                if data[mid]<=k: l=mid
                elif data[mid]>k: r=mid
            rb=r

        return rb-lb-1

if __name__ == '__main__':
    a = Solution()
    data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
    print(a.GetNumberOfK(data, 5))