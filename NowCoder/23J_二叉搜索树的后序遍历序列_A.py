#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/6


# 对于输入数组这种情况，使用指针作为下标，避免空间损耗
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        def recur(i,j):
            if i>=j: return True
            for p in range(i,j+1):
                if sequence[p]>sequence[j]:
                    break
            for m in range(p,j+1):
                if sequence[m]<sequence[j]:
                    break
            return m==j and recur(i,p-1) and recur(p,j-1)

        if not sequence: return False
        return recur(0,len(sequence)-1)