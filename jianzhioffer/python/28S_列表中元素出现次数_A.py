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
        k = self.weightList(numbers)
        n = len(numbers)
        if max(k) > n/2:
            index = k.index(max(k))
            return numbers[index]
        return 0
    # 输出res 与 L 同大小 元素为 原L中元素的个数
    def weightList(self, L):
        res = []
        n = len(L)
        for i in range(n):
            num = 0
            for j in range(n):
                if L[j] == L[i]:
                    num += 1
            res.append(num)
        return res

if __name__ == '__main__':
    a = Solution()
    l = [1,2,3,2,2,2,5,4,2]
    print(a.weightList(l))
    print(a.MoreThanHalfNum_Solution(l))
