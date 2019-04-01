# -*- coding: utf-8 -*-


n = int(input())
pointList = []
for i in range(n):
    s = input()
    a, b = list(map(int, s.split(' ')))
    pointList.append([a, b])
print(pointList)
lx, ly, lxy1, lxy2 = [], [], [], []
for i in pointList:
    lx.append(i[0])
    ly.append(i[1])
    lxy1.append(i[0]-i[1])
    lxy2.append(i[0]+i[1])

def repeatNum(l):
    res = []
    for i in range(len(l)-1):
        ll = []
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                ll.append(l.index(l[i]))
                ll.append(l.index(l[j]))
        res.append(list(set(ll)))
    return list(set(res))
lxNum = repeatNum(lx)
lyNum = repeatNum(ly)
lxy1Num = repeatNum(lxy1)
lxy2Num = repeatNum(lxy2)
