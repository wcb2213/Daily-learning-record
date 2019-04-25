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
        def TreeDepth(pRoot):
            # write code here
            if not pRoot:
                return 0
            else:
                leftx = self.TreeDepth(pRoot.left) + 1
                rightx = self.TreeDepth(pRoot.right) + 1
                x = max(leftx, rightx)
                return x

        if not pRoot:
            return True
        if abs(TreeDepth(pRoot.left) - TreeDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)