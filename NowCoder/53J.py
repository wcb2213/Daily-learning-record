#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/3/30


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        import re
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$",s)

    # def isNumeric(self, s):
    #     # write code here
    #     try :
    #         p = float(s)
    #         return True
    #     except:
    #         return False