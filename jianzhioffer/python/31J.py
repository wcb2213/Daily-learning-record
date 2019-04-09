#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        return ''.join(map(str, range(n+1))).count('1')