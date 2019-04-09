#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        currentStack = [root] ## 只有一个元素，root
        while currentStack:
            nextStack = []
            for i in currentStack:
                if i.left != None:  ##  if i.left:
                    nextStack.append(i.left)
                if i.right != None:
                    nextStack.append(i.right)
                res.append(i.val)
            currentStack = nextStack
        return res