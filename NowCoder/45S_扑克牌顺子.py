#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/26


# 30ms
# 扑克牌顺子
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers: return False
        dic,min_,max_={},14,0
        for i in numbers:
            if i==0: continue
            if i in dic: return False
            else:
                dic[i]=1
                if i<min_: min_=i
                if i>max_: max_=i
        return max_-min_<5


if __name__ == '__main__':
    a = Solution()
    l = [1,3,0,5,0]
    print(a.IsContinuous(l))