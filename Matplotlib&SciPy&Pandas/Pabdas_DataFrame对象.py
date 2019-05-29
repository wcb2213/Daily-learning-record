#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/29

import numpy as np
import pandas as pd

# 1 DataFrame对象生成
# Series对象构成的字典
s1 = pd.Series([1,2,3], index=['a','b','c'])
s2 = pd.Series([1.,2.,3.,4,], index=['a','b','c','d'])
d = {'one':s1, 'two':s2}
df = pd.DataFrame(d)
# print(df)
pd.DataFrame(d, index=['d','b','a'], columns=['two','three'])## select 'd','b','a' from tablename...;


