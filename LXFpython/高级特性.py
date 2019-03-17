#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/8/24


# 1 切片

# 0可省略L [0:3]取0 1 2 三个数
# L[::5] 所有数，每5个取一个
# [::] 第三个默认为1  且 正数 从前往后数 负数 从-1开始 从后往前
# 如[::-1] 从0到0 即全部 逆时 即逆序
# list tuple str
def trim(s):
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]==' ':  ## 取最后一个数 即L[-1]
        s=s[:-1] # 取第一个数到最后第二个数
    return s


# 2 迭代 iterable

# def findMinAndMax(L):
#     if L == []:
#         return (None, None)
#     min = max = L[0]
#     for i in L:
#         if min > i:
#             min = i
#         elif max < i:
#             max = i
#     return(min,max)

def findMinAndMax(L):
    if L == []:
        return(None,None)
    else:
        for a in L:
            for b in L:
                if a == min(L) and b == max(L):
                    return(a,b)

# def findMinAndMax(L):
#     if L == []:
#         return(None,None)
#     else:
#         return(min(L),max(L))


# 3 列表生成式
#   表达式+定义域
L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if type(s) == type('')]
L2 = [s.lower() for s in L1 if isinstance(s,(str))]
L3 = [str(s).lower() for s in L1 if isinstance(s, (str, int))]


# 4 生成器
第一种 列表生成式的[]改成()
第二种 函数 print改成yield

# def triangles(max):
#     L2 = [1]
#     n = 1
#     while max > n-1:
#         print(L2)
#         L1 = L2[:]
#         n = n+1
#         for i in range(1,n-1):
#             L2[i] = L1[i]+L1[i-1]
#         L2.append(1)
#     return 'done'

def triangles():
    L2 = [1]
    n = 1
    while 1:
        yield L2
        L1 = L2[:]
        n = n+1
        for i in range(1,n-1):
            L2[i] = L1[i]+L1[i-1]
        L2.append(1)
a = triangles(5)
for i in a:
    print(i)
    ## or next(a)

# 5 迭代器

1.凡是可作用于for循环的对象都是Iterable类型；

2.凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

3.集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

4.Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]: