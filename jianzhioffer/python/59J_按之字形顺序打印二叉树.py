#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/3


# 29ms
# 大家的实现很多都是将每层的数据存进ArrayList中，偶数层时进行reverse操作，
# 在海量数据时，这样效率太低了。
# （我有一次面试，算法考的就是之字形打印二叉树，用了reverse，
# 直接被鄙视了，面试官说海量数据时效率根本就不行。）
#
# 下面的实现：不必将每层的数据存进ArrayList中，偶数层时进行reverse操作，直接按打印顺序存入
# 思路：利用Java中的LinkedList的底层实现是双向链表的特点。
#  1)可用做队列,实现树的层次遍历
#  2)可双向遍历,奇数层时从前向后遍历，偶数层时从后向前遍历
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        stack = [pRoot]
        level = 1

        while len(stack) > 0:
            ns = []
            rs = []
            for i in stack:
                rs.append(i.val)
                if i.left:
                    ns.append(i.left)
                if i.right:
                    ns.append(i.right)

            if level % 2 == 0:
                rs.reverse()
            res.append(rs)

            stack = ns
            level += 1
        return res