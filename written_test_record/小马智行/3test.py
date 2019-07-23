#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/21


l_input = [2,0,1,3]
k = 1

# process
def f1(l, k, res):
    if len(l) == 2:
        if k%2==1:
            l.reverse()
            return res + l
        else:
            return res+l
    if k >= len(l)-1:
        n_max = max(l)
        res += [n_max]
        idx = l.index(n_max)
        l.pop
        return f1(l, k-idx, res)
    else:
        if k == 0:
            return res+l
        n_max = max(l[:k+1])
        res += [n_max]
        idx = l.index(n_max)
        l.pop
        return f1(l, k-idx, res)

print(f1(l_input, k, []))