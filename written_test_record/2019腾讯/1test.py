#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/7


n = 15
k = 4

a = n
b = 0
for i in range(k):
    a = (a+1)//2
    if a == 1:
        # b 为拆分次数
        b = i+1
# 若b为0，则经过k次拆分，然后一直减一到零
# 若b不为0，则经过b次拆分，a变为1，再做一次减一即可到零
if b != 0:
    print(b+1)
else:
    print(a+k)