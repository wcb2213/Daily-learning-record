#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/23


class Solution:
    def TreeDepth(self, pRoot):
        # write code here

        def recur(root, level):
            maxlevel = level
            if root.left != None:
                maxlevel = max(maxlevel, recur(root.left, level + 1))
            if root.right != None:
                maxlevel = max(maxlevel, recur(root.right, level + 1))
            return maxlevel

        if pRoot == None:
            return 0
        return recur(pRoot, 1)