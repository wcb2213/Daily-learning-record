#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/24


def process(s):
    n = len(s)
    if n % 2 == 1:
        return 'false'
    for i in range(int(n / 2)):
        if s[2 * i] != s[2 * i + 1]:
            return 'false'
    s1 = s[:int(n / 2)]
    s2 = s[int(n / 2):]
    s2 = s2[::-1]
    for i in range(int(n / 2)):
        if s1[i] != s2[i]:
            return 'false'
    return s[::2]


while True:
    try:
        s = input()
        print(process(s))
    except:
        break