#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/11


n = int(input())
bell = []
def hour2minute(h,m):
    return h*60+m
for i in range(n):
    tmp_list = list(map(int,input().split(' ')))
    bell.append(hour2minute(tmp_list[0],tmp_list[1]))
needTime = int(input())
tmp_list = list(map(int,input().split(' ')))
lessonTime = hour2minute(tmp_list[0],tmp_list[1])

for i in range(n - 1, -1, -1):
    if bell[i] <= lessonTime - needTime:
        break

res = divmod(bell[i], 60)
print(res[0],res[1])
