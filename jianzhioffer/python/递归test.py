#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/23


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

head = TreeNode(1)
p = head
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
# p.right.right = TreeNode(4)
p.left.right = TreeNode(5)
p.left.left.left = TreeNode(6)



def recur(root, level):
    maxlevel = level
    # print(maxlevel)
    if root.left != None:
        # maxlevel = recur(root.left, level + 1)
        maxlevel = max(maxlevel, recur(root.left, level + 1))  # 不加 按顺序执行 输出最右边的节点深度
        print(maxlevel)
    if root.right != None:
        # maxlevel = recur(root.right, level + 1)
        maxlevel = max(maxlevel, recur(root.left, level + 1))
        print(maxlevel)
    # print(maxlevel)
    return maxlevel

print(recur(head, 1))





