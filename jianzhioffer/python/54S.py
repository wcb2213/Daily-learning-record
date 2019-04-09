#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/31


class Solution:
    strl = ''

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        count = [0] * 256
        for s in self.strl:
            count[ord(s)] += 1

        for s in self.strl:
            if count[ord(s)] == 1:
                return s

        return '#'

    def Insert(self, char):
        # write code here
        self.strl = self.strl + char