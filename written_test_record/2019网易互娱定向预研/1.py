#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/11


# input
s = input().split(' ')
r = int(s[0])
g = int(s[1])
b = int(s[2])

# process
num = r//3 + g//3 +b//3
r -= (r//3)*3
g -= (g//3)*3
b -= (b//3)*3

# 若剩余的花环为 220 则增加两个彩花环，减少一个0对应的花环
if r+b+g == 4 and r*b*g == 0:
    print(num + 1)
else:
    print(num + min(r,g,b))