#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/23


# 665ms
# 旋转数组的最小数字
# 输入的是一个非减排序的数组的一个旋转  注意两点，非减 和 可不旋转
# 1.O(n)
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        return min(rotateArray)
# 2.O(logn) 二分法
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        l = rotateArray
        if len(l) == 0:
            return 0
        if len(l) == 1:
            return l[0]
        n = len(l)
        id1, id2, idx_mid = 0, n - 1, 0
        # 当旋转时, 无线循环，要加中断口
        while l[id1] >= l[id2]: #因为是非减序列，必须加等号
            if id2 - id1 == 1:
                return l[id2]
            if l[idx_mid] == l[id1] and l[idx_mid] == l[id2]:
                return min(l[id1:id2])
            idx_mid = (id1 + id2) // 2
            if l[idx_mid] >= l[id1]:
                id1 = idx_mid
            else:
                id2 = idx_mid
        # 当不旋转时，即l[0]
        return l[0]