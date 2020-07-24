#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/5


## 递归版本
# 时间复杂度：O(m+n)
# 空间复杂度：O(m+n),每一次递归，递归栈都会保存一个变量，最差情况会保存(m+n)个变量
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        ph1,ph2=pHead1,pHead2
        if ph1==None: return ph2
        if ph2==None: return ph1
        if ph1.val<=ph2.val:
            ph1.next=self.Merge(ph1.next, ph2)
            return ph1
        else:
            ph2.next=self.Merge(ph1, ph2.next)
            return ph2