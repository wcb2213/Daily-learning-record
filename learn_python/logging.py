#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/8


import logging
logging.basicConfig(level=logging.INFO) # 指定记录信息的级别，有debug，info，warning，error

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)