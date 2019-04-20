#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


# 25ms
# 跳台阶
class Solution:
    def jumpFloor(self, number):
        # write code here
        f1, f2 = 1 ,2
        if number == 1:
            return 1
        elif number == 2:
            return 2
        for i in range(3, number+1):
            a = f1 + f2
            f1 = f2
            f2 = a
        return a