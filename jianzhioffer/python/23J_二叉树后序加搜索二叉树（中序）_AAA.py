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
        root = sequence[-1] # 后序遍历最后一个数字是根节点
        n = len(sequence)
        for i in range(0, n): # >=i 为右子树，<i为左子树
            if sequence[i]>root:
                break
        # 下面这步是关键  判断是不是后序遍历
        for j in range(i, n): # 遍历右子树，所有值需大于 root值
            if sequence[j]<root:
                return False
        left = right = True
        if i > 0: # i=0 递归会报错
            left = self.VerifySquenceOfBST(sequence[0:i])
        if i < n-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right