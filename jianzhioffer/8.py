#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


class Solution:
    def jumpFloor(self, number):
        # write code here
        a = 1
        b = 1
        for i in range(number):
            a,b = b,a+b
        return a
