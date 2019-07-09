#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/8


class FooError(ValueError):
    pass

print('input your age:')
s = input()

n = int(s)
if n == 25:
    raise FooError('lalala')
print('your age is ', n)