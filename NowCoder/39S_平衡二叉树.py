#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/24


# 39ms
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 平衡二叉树：是一 棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def TreeDepth(p):
            if not p: return 0
            return 1 + max(TreeDepth(p.left), TreeDepth(p.right))

        if not pRoot: return True
        return abs(TreeDepth(pRoot.left) - TreeDepth(pRoot.right)) <= 1 \
               and self.IsBalanced_Solution(pRoot.left) \
               and self.IsBalanced_Solution(pRoot.right)