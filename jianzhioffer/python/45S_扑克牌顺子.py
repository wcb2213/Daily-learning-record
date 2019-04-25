#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/26


# 30ms
# 扑克牌顺子
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        l = sorted(numbers)
        # 去掉所有0
        zeroNum = 0
        for i in range(len(l)):
            if l[i] != 0:
                zeroNum = i
                break
        l = l[zeroNum:]
        # 有重复数字则False
        n = len(l)
        for i in range(n-1):
            if l[i] == l[i+1]:
                return False
        # max-min<=4 则True
        if l[-1] - l[0] <= 4:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    l = [1,3,0,5,0]
    print(a.IsContinuous(l))