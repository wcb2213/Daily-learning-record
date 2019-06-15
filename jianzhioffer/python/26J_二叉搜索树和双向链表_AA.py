#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


# 24ms
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        # l 利用list 按照中序顺序存储的链表地址 方便操作结点指针的指向
        l = self.get_midOrderList(pRootOfTree)
        n = len(l)
        l[0].left = None
        for i in range(n-1):
            l[i].right = l[i+1]
            l[i+1].left = l[i]
        l[n-1].right = None
        return l[0]

    # 得到二叉树的中序遍历的list
    def get_midOrderList(self, t):
        res = []
        if t.left:
            res += self.get_midOrderList(t.left)
        res.append(t)
        if t.right:
            res += self.get_midOrderList(t.right)
        return res