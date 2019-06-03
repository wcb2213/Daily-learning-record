#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


"""快速排序"""
# 最差时间分析	平均时间复杂度	稳定度	空间复杂度
# O(n2)	O(n*log2n)	不稳定	O(log2n)~O(n)
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(len(arr)//2) # 选取基准值，也可以选取第一个或最后一个元素,并从原始数组中移除基准值
        left, right = [], []
        for i in range(len(arr)):
            if arr[i] <= pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    array = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    print(quick_sort(array))