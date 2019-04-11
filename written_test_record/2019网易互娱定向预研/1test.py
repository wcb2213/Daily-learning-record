#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/11


r, g, b = 3, 6, 10

num = r//3 + g//3 +b //3
r -= (r//3)*3
g -= (g//3)*3
b -= (b//3)*3

if r+b+g == 4 and r*b*g == 0:
    print(num + 1)
else:
    print(num + min(r,g,b))