#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/9

import pysnooper

@pysnooper.snoop()
# n, sum = map(int, input().split(' '))
# list = list(map(int, input().split(' ')))
def f():
    n, sum = 5,10
    list = [5, 5, 10, 2, 3]
    list.sort()

    res = list.count(sum)
    count = 0
    i, j = 0, n-1
    while i<j:
        if list[i]+list[j]==sum:
            count += 1
            for k in range(i, j+1):
                if k == i or k == j:
                    count += 1
            break
        elif list[i]+list[j]<sum:
            i += 1
        elif list[i]+list[j]>sum:
            j -= 1
    print(res + count)
f()