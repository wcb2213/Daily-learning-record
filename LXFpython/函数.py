#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/8/24



# 1 调用函数

def int2str(n):
    return str(hex(n))

n1 = 255
n2 = 1000

print(int2str(n1))
print(int2str(n2))



# 2 定义函数

import math

def quadratic(a,b,c):
    # if not isinstance(a,b,c (int, float)):
    #     raise TypeError('bad operand type')
    if a == 0:
        print('不是二次函数')
    d = b*b-4*a*c
    if d >= 0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
    else:
        x1 = complex(-b, math.sqrt(-d))/(2*a)
        x2 = complex(-b, -math.sqrt(-d))/(2*a)
    return (x1,x2)
print(quadratic(1,1,3))



# 3 函数的参数

def product(*args):
    n = 1
    for i in args:
        n = n*i
    return n
print(product(1,2,3))



# 4 递归函数

# 第一种  观察fact(n)到fact(n-1)
#         确认fact(n)需要实现的功能
#         再用递归函数实现
def fact1(n):
    if n==1:
        return 1
    return n * fact1(n - 1)
print(fact1(5))

# 尾递归优化
def fact2(n,s=1):
    if n==1:
        return s
    return fact2(n-1,s*n)
print(fact2(5))

# 第二种 move(n,A,B,C)实现功能已知
#        与move(n-1,A,B,C)比较
#        从move(n-1,A,B,C)得到move(n,A,B,C)
def move(n,A,B,C):
    if n==1:
        print(A,'-->',C)
    else:
        move(n-1,A,C,B)#将a上前n-1个盘子从a移动到b上
        move(1,A,B,C)#将a最底下的最后一个盘子从a移动到c上
        move(n-1,B,A,C)#将b上的n-1个盘子移动到c上
n=int(input('请输入汉诺塔的层数：'))
move(n,'A','B','C')
