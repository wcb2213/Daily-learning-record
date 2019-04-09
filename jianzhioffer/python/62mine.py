#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 中序遍历(不用递归）可惜没给 self.next
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 最开始的节点
        if k <= 0 or not pRoot:
            return None
        while pRoot.left:
            pRoot = pRoot.left
        if k == 1:
            return pRoot
        for i in range(k-1):
            if not pRoot:
                return None
            pRoot = self.nextNode(pRoot)
        return pRoot.val

    def nextNode(self, p):
        if p.right:
            left = p.right
            while left.left:
                left = left.left
            return left
        while p.next:
            tmp = p.next
            if tmp.left == p:
                return tmp
            p = p.next
        return None