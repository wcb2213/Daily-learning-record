#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/28


# l1 = list(map(int, input().split(' ')))
# l2 = list(map(int, input().split(' ')))

l1 = [1, 3, 7, 4, 10]
l2 = [2, 1, 5, 8, 9]

l2.sort(reverse=True)
index = -1
for i in range(len(l1)-1):
    if l1[i] >= l1[i+1]:
        index = i
        break
if index == -1:
    print("NO")
else:
    num1, num2 = -1, -1
    if index > 0 and index < len(l1) - 2:
        selectRange = l1[index - 1:index + 3]
        for j in range(len(l2)):
            if l2[j] > selectRange[0] and l2[j] < selectRange[2] and num1 == -1:
                num1 = l2[j]
            if l2[j] > selectRange[1] and l2[j] < selectRange[3] and num2 == -1:
                num2 = l2[j]
            if num1 > -1 and num2 > -1:
                break
    elif index == 0:
        for j in range(len(l2)):
            if l2[j] < l1[1] and num1 == -1:
                num1 = l2[j]
            if l2[j] > l1[0] and l2[j] < l1[2] and num2 == -1:
                num2 = l2[j]
            if num1 > -1 and num2 > -1:
                break
    elif index == len(l1) - 2:
        for j in range(len(l2)):
            if l2[j] > l1[-3] and l2[j] < l1[-1] and num1 == -1:
                num1 = l2[j]
            if l2[j] > l1[-2] and num2 == -1:
                num2 = l2[j]
            if num1 > -1 and num2 > -1:
                break
    if num1 == -1 and num2 == -1:
        print("NO")
    else:
        if num1 > num2:
            l1[index] = num1
        else:
            l1[index + 1] = num2
        print(' '.join(map(str, l1)))