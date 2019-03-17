#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]  ##后序遍历最后一个数字是根节点
        n = len(sequence)
        for i in range(0, n): ##找到右子树的第一个节点
            if sequence[i]>root:
                break
        for j in range(i, n): ##二叉树排列左节点小于根节点小于右节点
            if sequence[j]<root:
                return False
        left = right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        if i < n-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right