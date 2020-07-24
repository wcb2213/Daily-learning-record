#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


# 25ms
# 二叉搜索树（中序遍历）的常规做法
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 中序 左根右 递归
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        def midRecur(p):
            if not p: return None
            midRecur(p.left)
            res.append(p)
            midRecur(p.right)

        res = []
        midRecur(pRoot)
        if k < 1 or k > len(res): return
        return res[k - 1]