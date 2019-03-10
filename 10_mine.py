#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24


class Solution:
    def rectCover(self, number):
        # write code here
        n = number
        if n == 0:
            return 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a, b = 1, 2
        for i in range(3,n+1):
            a ,b = b, a+b
        return b