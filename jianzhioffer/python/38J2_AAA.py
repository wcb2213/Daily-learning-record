#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/24

class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        else:
            leftx = self.TreeDepth(pRoot.left) + 1
            rightx = self.TreeDepth(pRoot.right) + 1
            x = max(leftx, rightx)
            return x