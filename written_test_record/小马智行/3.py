#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/21


# input
t = int(input())
nl, kl, inl =[], [], []
for i in range(t):
    nl.append(int(input()))
    kl.append(int(input()))
    inl.append(list(map(int, input().split(' '))))
# print(inl)

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
        l.pop(idx)
        return f1(l, k-idx, res)
    else:
        if k == 0:
            return res+l
        n_max = max(l[:k+1])
        res += [n_max]
        idx = l.index(n_max)
        l.pop(idx)
        return f1(l, k-idx, res)

# output
for i in range(t):
    print(f1(inl[i], kl[i], []))