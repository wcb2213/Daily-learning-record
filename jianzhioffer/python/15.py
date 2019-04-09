#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/26


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # if not pHead or not pHead.next:
        #     return pHead
        last = None
        while pHead: #假设pHead 为 ｛1，2，3｝
            tmp = pHead.next #可以理解为创建了新的一个栈 ｛2，3｝
            pHead.next = last #本来地址指向后面的2 现在指向前面的last
            last = pHead #last为一个新栈 ｛1｝ 继承pHead的当前值1 和地址 前面的last 刚好反向连接
            pHead = tmp #pHead 变为｛2，3｝ 相当于抛出 1 继续循环
        return last