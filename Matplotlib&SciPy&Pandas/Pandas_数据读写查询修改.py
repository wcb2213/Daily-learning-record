#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/6/2

import numpy as np
import pandas as pd

## 数据读写
s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([1.,2.,3.,4,], index=['a','b','c','d'])
d = {'one':s1, 'two':s2}
df = pd.DataFrame(d)

# df.to_csv('foo.sql')
data = pd.read_csv('foo.csv', index_col=0)
print(data)

data.columns
# print(data.columns)
## 数据查询
hou = (data.bar2 == 2.0)
data.loc[hou, ['one', 'bar']]
print(data.loc[hou, ['one', 'bar']])