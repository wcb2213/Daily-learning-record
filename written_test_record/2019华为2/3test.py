#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/24


s = 'oNEthrEEfoursixNiNENiEN'
s=input()
s = s.lower()
dict={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

l =[]
def process(s):
    if s == '':
        return
    if s[0] == 'z':
        l.append(0)
        return process(s[4:])
    if s[0] == 'o':
        l.append(1)
        return process(s[3:])
    if s[0] == 't':
        if s[1] == 'w':
            l.append(2)
            return process(s[3:])
        else:
            l.append(3)
            return process(s[5:])
    if s[0] == 'f':
        if s[1] == 'o':
            l.append(4)
            return process(s[4:])
        else:
            l.append(5)
            return process(s[4:])
    if s[0] == 's':
        if s[1] == 'i':
            l.append(6)
            return process(s[3:])
        else:
            l.append(7)
            return process(s[5:])
    if s[0] == 'e':
        l.append(8)
        return process(s[5:])
    if s[0] == 'n':
        l.append(9)
        return process(s[4:])
process(s)
print(''.join(map(str,l)))
