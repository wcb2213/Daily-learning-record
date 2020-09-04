#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/8/26


#   1   分别排序
def minMeetingRooms(begins, ends):
    begins.sort()
    ends.sort()
    room=0
    endIdx=0
    for a in begins:
        if a>ends[endIdx]:
            endIdx+=1
        else:
            room+=1
    return room

if __name__=="__main__":
    arr=[[0,6], [4,14], [8,24], [16,22], [20,26]]
    begins=[x[0] for x in arr]
    ends=[x[1] for x in arr]
    print(minMeetingRooms(begins,ends))