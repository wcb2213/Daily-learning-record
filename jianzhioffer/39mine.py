#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/24


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