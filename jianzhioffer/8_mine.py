#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


class Solution:
    def jumpFloor(self, number):
        # write code here
        f1, f2 = 1 ,2
        if number == 1:
            return 1
        elif number == 2:
            return 2
        while number-2:
            a = f1 + f2
            f1 = f2
            f2 = a
            number = number-1
        return a

# 运行时间：21ms
#
# 占用内存：5844k