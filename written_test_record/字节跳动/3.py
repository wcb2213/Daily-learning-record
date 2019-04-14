#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/14


#### 示例有问题吧 到底有没有比例系数
from functools import reduce
n = int(input())
l_input = list(map(int, input().split(' ')))
# print(l_input)
# l_input = [1, 6, 4]

l_input.append(0)
l_input.reverse()
def f1(a, b):
    return (a+b)/2
print(reduce(f1,l_input))
