#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/6/14


"""归并排序"""
# 时间复杂度（平均）	时间复杂度（最坏)	时间复杂度（最好)	空间复杂度	稳定性	复杂性
# O(nlog2n)O(nlog2n)	O(nlog2n)O(nlog2n)	O(nlog2n)O(nlog2n)	O(n)O(n)	稳定	较复杂
def MergeSort(lists):
    if len(lists) < 2:
        return lists
    num = len(lists) // 2
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right): # 两个有序列表合成一个有序列表
    r, l=0, 0
    res=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += list(left[l:])
    res += list(right[r:])
    return res

if __name__ == '__main__':
    lists = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    print(MergeSort(lists))