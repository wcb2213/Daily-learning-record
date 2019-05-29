#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/29

import numpy as np
import pandas as pd

# 1 生成series对象
# 利用数组
a = pd.Series([1,2,3,4])
# print(a)#左边是标记，右边是对应的数据，index 默认 range(n)
# print(a.index)#包含start 不包含end
a2 = pd.Series([1,2,3,4], index=['a','b','c','d'])
a2['b']
# print(a2['b'])#索引
# 利用字典
d = {'c':3, 'b':2, 'a':1}
pd.Series(d)
pd.Series(d, index=('c','d','b','e'))# index 用于指定顺序 不存在的键对应np.nan
# print(pd.Series(d, index=('c','d','b','e')))# index 用于指定顺序 不存在的键对应np.nan
# 利用标量
pd.Series(5, index=range(3))


# 2 series对象使用
# 数组
s = pd.Series(np.array(range(5)), index=['a','b','c','d','e'])
# print(s)
s[0]
s[:3]
s[s > s.median()]
s[[4,3,1]]
np.exp(s)## 重要 类似map
#字典
s['a']
s['e']=12
'e' in s
# 向量化操作
s + s
s * 2
np.exp(s)
s[1:] + s[:-1] # 这个与数组不同，因为series是有标记的，相同标记的相加，不同的赋值np.nan再相加
s.name