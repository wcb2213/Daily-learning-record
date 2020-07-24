#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21

# 42ms
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# python 中好像有内置函数 下次看一下
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        we={}
        thre=(len(numbers)+1)//2 if len(numbers)%2==1 else len(numbers)//2+1
        for i in numbers:
            if i in we:
                we[i]+=1
            else:
                we[i]=1
            if we[i]>=thre:
                return i
        return 0

if __name__ == '__main__':
    a = Solution()
    l = [1,2,3,2,2,2,5,4,2]
    print(a.MoreThanHalfNum_Solution(l))
