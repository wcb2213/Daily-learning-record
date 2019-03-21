#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/2/2


import math
from collections import Iterable
from collections import Iterator
from functools import reduce
# 5/15  函数的返回值

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():  # 继承参数 一种是 count（）的 也可以是 for i 。。
#              return i*i
#         fs.append(f)
#     return fs
#
# # f1, f2, f3 = count()
# counterA = count()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()

# 注意 不是 1 4 9 而是 9 9 9   返回函数会继承原来函数的参数，但是继承的
# 参数为返回函数执行时的参数
# 对于返回函数继承的参数 主要注意一下

# 继承参数 实例
# def count():
#     def f(j): # f(j) 不是闭包
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs

# def count():
#
#     def f(): #会报错 因为 f() 没有继承到参数
#          return i*i
#
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs

# f1, f2, f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

# def createCounter():
#     data = [0]
#     def counter():
#         data[0] += 1
#         return data[0]
#     return counter
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')


# 5/20

# L = list(filter(lambda x:x%2 ==1, range(1, 20)))
# print(L)


# 5/22
# import functools
# import time
#
#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         strat = time.time()
#         func = fn(*args, **kw)
#         end = time.time()
#         print('%s executed in %s ms' % (fn.__name__, end - strat))
#         return func
#     return wrapper
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# 5/23
# int() #base 默认为10  想改成默认为2
# def int2(x, base = 2):
#     return int(x, base)

# 8/21
# # 抛错
# # def my_abs(x):
# #     if not isinstance(x, (int, float)):
# #         raise TypeError('bad operand type')
# #     if x >= 0:
# #         return x
# #     else:
# #         return -x
#
# # def person(name, age, **kw):
# #     print('name:', name, 'age:', age, 'other:', kw)
# #
# # person('Bob', 35, city='Beijing')
#
#


# #  算法优化 尾递归
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# # 如果我们计算fact(5)，可以根据函数定义看到计算过程如下：
# #
# # ===> fact(5)
# # ===> 5 * fact(4)
# # ===> 5 * (4 * fact(3))
# # ===> 5 * (4 * (3 * fact(2)))
# # ===> 5 * (4 * (3 * (2 * fact(1))))
# # ===> 5 * (4 * (3 * (2 * 1)))
# # ===> 5 * (4 * (3 * 2))
# # ===> 5 * (4 * 6)
# # ===> 5 * 24
# # ===> 120
#
# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
# # ===> fact_iter(5, 1)
# # ===> fact_iter(4, 5)
# # ===> fact_iter(3, 20)
# # ===> fact_iter(2, 60)
# # ===> fact_iter(1, 120)
# # ===> 120



8/22
# # 切片 相当于 L[0:3] 注意 0:3 取三个数 而不是四个
# # 索引值 0  可以忽略
# # 可用于 字符串 list tuple
# L = [1,2,3,4]
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
# print(r)
# print(L[0:3])


# # 迭代和列表生成式
# # 迭代 字符串 list tuole dict（默认 key d.values() d.items()）
# # 列表生成式 = 函数表达式（x） + 迭代（x定义域）
# L = ['Hello', 'World', 'IBM', 'Apple']
# # r = [s.lower() for s in L]
# r = [x * x for x in range(1, 11) if x % 2 == 0]
# print(r)


# # 生成器 一边循环一边计算的 列表生成式 generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# for n in fib(6):
#     print(n)



# # 函数式编程
# # def f(x):
# #     return x * x
# # r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# # print(list(r))
#
#
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
# # 此处lambda是第二种用法
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
#
# # 打印1000以内的素数:
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# 匿名函数
# 第一种 lambda x: x+1 / 变量：函数表达式
# 匿名函数 lambda 第二种用法
# def is_odd(n):
#     return n % 2 == 1
#
# L = list(filter(is_odd, range(1, 20)))
# print(L)
#
# R = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# print(R)
# 第三种 作为函数返回值
# def build(x, y):
#     return lambda: x * x + y * y

# 返回函数 的闭包问题
# def count():
#     def f(j):
#         # def g():
#         #     return j*j
#         # return g
#         return lambda: j*j
#     fs = []
#     print(fs)
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(f1(),f2(),f3())


#装饰器
# import functools
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrappe
# import functools
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


# import functools
# import time
#
#
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         strat = time.time()
#         r = fn(*args, **kw)
#         end = time.time()
#         print('%s executed in %s ms' % (fn.__name__, (end-strat)*1000))
#         return r
#     return wrapper
#
# @metric
# def now():
#     print('2015-3-25')
#
# now()


# # 偏函数 改变默认参数
# print(int('12345',base=8))
#
# def int2(x, base=8):
#     return int(x, base)
# print(int2('12345'))
#
# import functools
# int22 = functools.partial(int, base=8)
# print(int22('12345'))



#8/24
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
# __init__ 的定义 每个对象需要 name 及 score 两个属性 不能缺少
# 但可以自定义增加
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
#
# # student没有定义age数据参数 但是python支持绑定任意数据参数
# bart.age = 8
#
# print('%s: %s' %(lisa.name, lisa.get_grade()))
# print(bart.name, bart.get_grade())
# print(bart.age)


# class Animal(object):
#
#     def run(self):
#         print('Animal is running...')
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# run_twice(Animal())
#
# dog = Dog()
# run_twice(dog)
#
# cat = Cat()
# run_twice(cat)


# 判断类型
# print(type(123)==int)
# import types
# def fn():
#     pass
#
# print(type(fn)==types.FunctionType)
#
# print(type(abs)==types.BuiltinFunctionType)
#
# print(type(lambda x: x)==types.LambdaType)
#
# print(type((x for x in range(10)))==types.GeneratorType)

# h 为 对象 Husky 为类
# isinstance(h, Husky)
# 判断是否是list或者tuple
# isinstance([1, 2, 3], (list, tuple))

# dir 获取一个对象的所有属性和方法
# print(dir('ABC'))

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19

# >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 404
# 也可以获得对象的方法：
#
# >>> hasattr(obj, 'power') # 有属性'power'吗？
# True
# >>> getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# >>> fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn() # 调用fn()与调用obj.power()是一样的
# 81

# 实例属性和类属性
# >>> class Student(object):
# ...     name = 'Student'
# ...
# >>> s = Student() # 创建实例s
# >>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
# >>> print(Student.name) # 打印类的name属性
# Student
# >>> s.name = 'Michael' # 给实例绑定name属性
# >>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
# >>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
# >>> del s.name # 如果删除实例的name属性
# >>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        strat = time.time()
        r = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end-strat)*1000))
        return r
    return wrapper

@metric
def now():
    print('2015-3-25')

now()


