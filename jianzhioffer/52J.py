#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/29


#正则表达式 及 re模块
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        import re
        k = re.findall(pattern, s)
        if s in k:
            return True
        else:
            return False