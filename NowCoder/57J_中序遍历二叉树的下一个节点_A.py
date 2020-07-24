#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


# 27ms
# 二叉树的下一个节点
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
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
        p=pNode
        if not p: return p
        # 是否有右节点，有则左中右
        while p.right:
            res=p.right
            while res.left:
                res=res.left
            return res
        # 是否有父节点，有则
        while p.next:
            res=p.next
            if res.left==p:
                return res
            p=res
        # 均无，说明最后一个节点
        return None