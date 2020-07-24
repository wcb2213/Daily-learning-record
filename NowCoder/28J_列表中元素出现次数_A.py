#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/11


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        cnt=0
        for i in numbers:
            if cnt==0: res=i
            if i==res: cnt+=1
            else: cnt-=1
        return res if numbers.count(res)*2>len(numbers) else 0