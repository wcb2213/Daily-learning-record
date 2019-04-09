#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


# 1、有右子树的，那么下个结点就是右子树最左边的点
# 2、没有右子树的，也可以分成两类，
#     a)是父节点左孩子，那么父节点就是下一个节点 ；
#     b)是父节点的右孩子，找他的父节点的父节点的父节点...直到当前结点是其父节点的左孩子位置。若没有，那么当前节点是尾节点。
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        # 1
        if pNode.right:
            left = pNode.right
            while left.left:
                left = left.left
            return left
        # 2
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
            pNode = pNode.next
        # 若没有，那么当前节点是尾节点
        return None