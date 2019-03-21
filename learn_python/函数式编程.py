#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/8/28


# 1 高阶函数

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# map
a = [1,2,3]
r = map(lambda x: x*x, a)
print(list(r))
print(tuple(r))
print(list(r))
print(a)   #map传出的对象是 iterator ，故使用后 r 中已经没有对象了
# def normalize(name):
#     s = name.lower()
#     l = list(s)
#     t = s[:1]
#     l[0] = t.upper()
#     return ''.join(l)

def normalize(name):
    return name[0].upper()+name[1:].lower()

def normalize(name):
    return name.capitalize()

# reduce
from functools import reduce

# def prod(L):
#     def f(x, y):
#         return x * y
#     return reduce(f, L)

def prod(L):
    return reduce(lambda x, y: x * y, L)

def str2float(s):
    s1 = s.split('.')[0]
    s2 = s.split('.')[1]
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    def fn(x, y):
        return x * 10 + y
    def str2int(s):
        return reduce(fn, map(char2num,s))
    num = float(str(str2int(s1))+'.'+str(str2int(s2)))
    return num

# filter
def is_palindrome(n):
    s1 = str(n)
    return s1 == s1[::-1]

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# def primes():
#     yield 2 #返回 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数 即 3
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
#
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# sorted
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score, reverse = True)
print(L2, L3)


# 2 返回函数
# f1, f2, f3调用闭包函数
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()

print(f1(), f2(), f3())
print(isinstance(f1(),int)) # int 类型？

# counterA(), counterA(), counterA(), counterA(), counterA()调用函数
# counterB()重新执行函数
def createCounter():
    x = (x for x in range(1,100))
    def counter():
        return next(x)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')