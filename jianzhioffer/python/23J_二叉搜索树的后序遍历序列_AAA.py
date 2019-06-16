#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


# 23ms
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果
# 二叉搜索树，即中序遍历
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        def recur(list1):
            if not list1:
                return True
            root = list1[-1]
            n = len(list1)
            for i in range(n): ## 必须取n 因为可能不存在左子树
                if list1[i] > root:
                    break
            for j in range(i, n):
                if list1[j] < root:
                    return False
            return recur(list1[:i]) and recur(list1[i:-1])

        return recur(sequence)