#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/25


def bubble(l):
    l_len = len(l)
    for j in range(l_len-1):
        for i in range(l_len-1-j):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l


if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    print(bubble(bubbleList))
