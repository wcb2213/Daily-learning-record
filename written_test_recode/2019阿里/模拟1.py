#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/9


sIn1 = '<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>'
sIn2 = '来几首@{singer}的流行歌曲'
l1, l2, l3, l4, l5 = [], [], [], [], []
for i in range(len(sIn1)):
    if sIn1[i] == '<':
        l1.append(i)
    if sIn1[i] == '>':
        l2.append(i)

# s1 = '[]' s2 = '|'
s1, s2 = [], []
for i in range(len(l1)):
    for j in range(int(l1[i])+1, int(l2[i])):
        if sIn1[j] == '[':
            l3.append(i)
        if sIn1[j] == ']':
            l4.append(i)
        if sIn1[j] == '|':
            l5.append(i)
        for k in range(len(l3)):
            s1.append(sIn1[int(l3[i])+1: int(l4[i])])
        for l in range(len(l5)):
            while sIn1[int(l5[l])-1] != '<' and sIn1[int(l5[l])-1] != '>' and sIn1[int(l5[l])-1] != '[' and sIn1[int(l5[l])-1] != ']' and sIn1[int(l5[l])-1] != '|':
                s2.append()