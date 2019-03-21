#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/8/24


# 8/24 函数

1 格式化字符串
# 占位符	替换内容
# %d	整数
# %f	浮点数   0.2f 即保留两位小数
# %s	字符串
# %x	十六进制整数

# s = 'Hi, %s, you have $%d.' % ('Michael', 1000000)
# print(s)

2 hex(n)
# 将n转化为16进制表示


3 复数
# print(complex(1,2))
# #类型为 complex


4 input 和 split
# n=input('请输入汉诺塔的层数：')
# print(n)
# print(isinstance(n,str))
# #input()输入为一行所有值，默认输入为str
# # 请输入汉诺塔的层数：12415 \n 251515
# # 12415 \n 251515
# # True

# str.split(str="", num=string.count(str)).
# s = input('用空格分隔多个数据:')
# n = [int(n) for n in s.split()]
# print(n)
# for n in s.split(' ', -1): # -1表示all 1 表示分成两个str
#     print(n)

5 print 输出不换行及多个输入之间无空隙
# print('1','2','3', end ='')
# print('1','2','3')
# print('1','2','3',sep = '')

# 8/27 高级特性
6 数组复制
L1 = L2
当L2改变时 L1会跟着改变
若需要L1不跟着改变
L1 = L2[:]#相当于把L2中的全部切片赋给L1

7 函数报错弹出
# # a = 2
# # isinstance(a,int)      # 结果返回 True
# s='wfwef'
# if isinstance(s,(str)):
#     raise TypeError('这货是个字符串，所以报错了')


# 8/28 函数式编程

8 str.join(sequence)
# str = "-"
# seq = ("a", "b", "c") # 字符串序列
# print(str.join( seq ))
# # '''a-b-c
扩展：数组元素合并
# list=['1','2','3','4','5']
# print(''.join(list))
# # '''12345 str

9 lambda
# add = lambda x, y: x * 10 + y
# print(add(1,3))

扩展：结合reduce（即重复作用）和map函数（分别作用）

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
# def char2num(s):
#     return DIGITS[s]
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#     #### lambda x, y: x * 10 + y 作为匿名函数 map(char2num, s)映射数组[1,2,3] reduce 重复作用。。。 结论:优秀
# print(str2int('123'))
# # 123

10 字典
# a={'a':1,'b':[2]}
# a['a']=3
# a['c']=3
# print(a)
# a['b'].append(4)
# print(a)
# # {'a': 3, 'b': [2], 'c': 3}
# # {'a': 3, 'b': [2, 4], 'c': 3}

12 切片
L[-1::-1]=L[::-1]
# l = [1,2,3,4,5]
#
# print(l[-1::-1])
# print(l[::-1])

# 19/3/12
13 输出迭代数列的下标和元素
# enumerate(sequence, [start=0])
# seq = ['one', 'two', 'three']
# for i, element in enumerate(seq, start=1): #start 为起始index 默认为 0
#     print(i, element)
# # ...
# # 1 one
# # 2 two
# # 3 three

14 sorted() 排序函数
sorted(iterable[, cmp[, key[, reverse]]])

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# # ['Zoo', 'Credit', 'bob', 'about'] 倒序排列 key 不改变原值
# # 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

进阶
key : 选择元素要比较的形式
cmp : 两两比较，如果返回为正，则交换两者的位置，即y在前x在后，否则x在前y在后
默认 cmp = lambda x,y: x-y
# L=[('b',2),('a',1),('c',3),('d',4)]
# sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
# sorted(L, key=lambda x:x[1])               # 利用key

15 filter() 筛选函数
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# def is_odd(n):
#     return n % 2 == 1
# list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# # 结果: [1, 5, 9, 15]


19/3/19
16 知道数组的val 查找下标
# L = [1,2,3]
# for i in range(len(L)):
#     print(L.index(3-i))

19/3/21
17 count() 字符串计数
str.count(sub, start= 0,end=len(string))
# str="ooo...o"
# sub='o'
# print ("str.count('o') : ", str.count(sub, 0, 7)) # 4
# print ("str.count('o') : ", str.count(sub, 0, 6)) # 3