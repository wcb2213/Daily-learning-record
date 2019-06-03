#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/6/3


"""选择排序"""
# 最差时间分析	平均时间复杂度	稳定度	空间复杂度
# O(n2)	O(n2)	不稳定	O(1)
# 算法稳定性指 在待排序的数据中，存在多个相同的数据，经过排序之后，他们的对相对顺序依旧保持不变
def findSamllest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def select_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSamllest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr


if __name__ == '__main__':
    array = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    print(select_sort(array))