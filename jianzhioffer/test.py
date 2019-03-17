#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/26

#
# t1=1,2,3
# t2="jeffreyzhao","cnblogs"
# t3=(1,2,3,4)
# t4=()
# t5=(1,)
# print(t1,t2,t3,t4,t5)


# l = list(123)
# print(l)

# str1='Hello world'
# print(str1)
# print(str1[0])
# for c in str1:
#     print(c)

# str1='Hello,%s' % 'world.'
# print(str1)
# strs=('Hello','world') #元组
# str2='%s,%s' % strs
# print(str2)
# d={'h':'Hello','w':'World'} #字典
# str3='%(h)s,%(w)s' % d
# print(str3)

# str1='%s,%s' % ('Hello', 'world')
# print(str1)

# str1='%s%%' % 100
# print(str1)

# from math import pi
# str1='%.2f' % pi #精度2
# print(str1)
# str2='%10f' % pi #字段宽10
# print(str2)
# str3='%10.2f' % pi #字段宽10，精度2
# print(str3)

# from string import Template
# str1=Template('$x,$y!')
# str1=str1.substitute(x='Hello',y='world')
# print(str1)

# 如果替换字段是单词的一部分，那么参数名称就必须用括号括起来，从而准确指明结尾：

# from string import Template
# str1=Template('Hello,w${x}d!')
# str1=str1.substitute(x='orl')

# from string import Template
# str1=Template('$x$$')
# str1=str1.substitute(x='100')
# print(str1)

# from string import Template
# d={'h':'Hello','w':'world'}
# str1=Template('$h,$w!') #必须 x, y
# str1=str1.substitute(d)
# print(str1)

# 4、通用序列操作（方法）
# 从列表、元组以及字符串可以“抽象”出序列的一些公共通用方法（不是你想像中的CRUD），这些操作包括：
# 索引（indexing）、分片（sliceing）、加（adding）、乘（multiplying）以及检查某个元素是否属于序列的成员。
# 除此之外，还有计算序列长度、最大最小元素等内置函数。

# （1）索引

# （2）分片
# nums=range(10)
# print nums
# print nums[1:5]
# print nums[6:10]
# print nums[1:]
# print nums[-3:-1]
# print nums[-3:] #包括序列结尾的元素，置空最后一个索引
# print nums[:] #复制整个序列
# print nums[0:10:2]  #步长为2
# 输出：
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4]
# [6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [7, 8]
# [7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 2, 4, 6, 8]

# （3）序列相加
#
# str1='Hello'
# str2=' world'
# print str1+str2
# num1=[1,2,3]
# num2=[2,3,4]
# print num1+num2
# print str1+num1
# 输出：
#
# Hello world
# [1, 2, 3, 2, 3, 4]
#
# Traceback (most recent call last):
#   File "F:\Python\test.py", line 7, in <module>
#     print str1+num1
# TypeError: cannot concatenate 'str' and 'list' objects

# （4）乘法
# print [None]*10
# str1='Hello'
# print str1*2
# num1=[1,2]
# print num1*2

# （5）成员资格
# in运算符会用来检查一个对象是否为某个序列（或者其他类型）的成员（即元素）：
# str1='Hello'
# print 'h' in str1
# print 'H' in str1
# num1=[1,2]
# print 1 in num1

# （6）长度、最大最小值
# 通过内建函数len、max和min可以返回序列中所包含元素的数量、最大和最小元素。

a = b = 1
print(a, b)