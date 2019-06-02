#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/29

import numpy as np
import pandas as pd

# 1 DataFrame对象生成
# 1.1 Series对象构成的字典
s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([1.,2.,3.,4,], index=['a','b','c','d'])
d = {'one':s1, 'two':s2}
df = pd.DataFrame(d)
# print(df)
pd.DataFrame(d, index=['d','b','a'], columns=['two','three'])## select 'd','b','a' from tablename...;
# 1.2 使用以为数组构成的字典生成
d = {'one': [1, 2, 3, 4],
     'two': [4, 3, 2, 1]}
pd.DataFrame(d)
pd.DataFrame(d,index=['a','b','c','d'])

## 1.3 使用结构数组生成？？

# 1.4 使用字典数组生成
data2 = [{'a':1, 'b':2}, {'a':5, 'b':10, 'c':20}]
pd.DataFrame(data2)


# 2 DataFrame对象使用
# 2.1 列操作
s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([1.,2.,3.,4,], index=['a','b','c','d'])
d = {'one':s1, 'two':s2}
df = pd.DataFrame(d)
df['one']
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
# print(df)
del df['two']
df.pop('three')
# print(df)
df.insert(1,'bar',df['flag'])
df.insert(1,'bar2',s1)
# print(df)
# 2.2 行 如选择第二行有两种办法
df.loc['b']
df.iloc[1]
# 2.3 加法和减法操作

## 数据读写
df.to_csv('foo.sql')
pd.read_csv('foo.csv')