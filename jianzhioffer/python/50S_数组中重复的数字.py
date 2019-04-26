#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


# 27ms
# 数组中重复的数字
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if numbers[i] == numbers[j]:
                    duplication[0] = numbers[i]
                    return True
        return False

if __name__ == '__main__':
    a = Solution()
    l1 = [2,1,3,1,4]
    l2 = [-1]
    print(a.duplicate(l1, l2), l2[0])