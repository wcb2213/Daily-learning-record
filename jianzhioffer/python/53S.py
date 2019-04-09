#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/3/30


import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",s)