#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        result=[]
        if not ss:
            return []
        else:
            res=itertools.permutations(ss)
            for i in res:
                if "".join(i) not in result:
                    result.append("".join(i))
        return result

    # def Permutation(self, ss):
    #     # write code here
    #     return [] if not ss else sorted(list(set(map(lambda s:''.join(s), itertools.permutations(ss)))))