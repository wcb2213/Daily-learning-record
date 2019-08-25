#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/24


def go_run(start):
    def step(step):
        # 申明start不是当前局部变量
        nonlocal start
        start += step
        return start

    return step


run = go_run(0)
# 跑了3步
total_run = run(3)
print(total_run)
# 又跑了5步
total_run = run(5)
print(total_run)