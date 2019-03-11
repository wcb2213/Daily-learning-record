#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/10


import sys
a=b=c=d=0
for line in sys.stdin:
    offset,n,l1,l2=map(int,line.split())
def f(offset,n,l1,l2):
    o=offset
    if o<l1:#l1 start
        if o+n<=l1+l2:#disp all
            if o+n<=l1:#only l1 disp
                a=o
                b=o+n
                c=0
                d=0
            else:##l1 l2 disp
                a=o
                b=l1
                c=0
                d=n-(l1-o)
        else:
            a=o
            b=l1
            c=0
            d=l2
    elif o >= l1:## start from l2
        if o+n<=l1+l2:#disp all
            a=l1
            b=l1
            c=o-l1
            d=o-l1+n
        else:
            a=l1
            b=l1
            c=o-l1
            d=l2
    print(a,b,c,d)
    return(a,b,c,d)
# print(f(2,4,4,4))
# print(f(1,2,4,4))
# print(f(4,1,3,3))
f(offset,n,l1,l2)


