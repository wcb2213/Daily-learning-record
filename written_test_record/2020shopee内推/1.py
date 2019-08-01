#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/25


# s1,s2 = input().split(' ')
s1 = "abcabc"
s2 = "abcabcabc"
if len(s1)<len(s2):
    s1,s2 = s2,s1

if s1 == s2:
    print(s2)
tmp = []
for i in range(len(s2),0,-1):
    if len(s1)%i == 0:
        tmp.append(i)
for i in tmp:
    if i == len(s2) and s1[:i*2]==s2*2:
        print(s2)
        break
    elif s1[:i*2]==s2[:i*2]:
        print(s1[:i])
        break