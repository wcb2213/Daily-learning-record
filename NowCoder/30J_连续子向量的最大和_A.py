#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/24


# dp[i]指终止下标为i的连续子数组的最大和，如dp[2]=6-3-2=1
# 由于转移方程只有dp[i-1]与dp[i]，因此课用tmp表示这个过程，空间复杂度为O（1）
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        tmp,res=array[0],array[0]
        for i in range(1,len(array)):
            tmp = array[i]+max(tmp,0)
            res = max(res,tmp)
        return res

if __name__ == '__main__':
    a = Solution()
    l = [6,-3,-2,7,-15,1,2,2]
    print(a.FindGreatestSumOfSubArray(l))