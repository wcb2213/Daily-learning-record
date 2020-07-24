#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/15

# 30ms
# 输入两棵二叉树A，B，判断B是不是A的子结构 （注意：当B空，A可不为空）
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## 一般返回bool类型的递归程序，&& 与 || 的灵活使用，可以使代码非常简洁。
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here

        def recur(pr1,pr2):
            if not pr2: return True
            if not pr1 or pr1.val!=pr2.val: return False
            return recur(pr1.left, pr2.left) and recur(pr1.right, pr2.right)

        pr1,pr2=pRoot1,pRoot2
        if not pr1 or not pr2: return False
        return recur(pr1,pr2) or self.HasSubtree(pr1.left, pr2) or self.HasSubtree(pr1.right, pr2)