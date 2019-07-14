#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


# 25ms
# 数组中重复的数字
# 书T3
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        i=0
        while i<len(numbers):
            if numbers[i]!=i:
                if numbers[i]==numbers[numbers[i]]:
                    duplication[0]=numbers[i]
                    return True
                else:
                    tmp = numbers[i]
                    numbers[i],numbers[tmp] = numbers[tmp], numbers[i]
            i += 1
        return False