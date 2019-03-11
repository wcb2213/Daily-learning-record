#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/14

# 运行时间：21ms
#
# 占用内存：5856k
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s)

        n = len(s)
        for i in range(n):
            if s[i]==' ':
                s[i]='%20'
        return ''.join(s)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# str = "-";
# seq = ("a", "b", "c");  # 字符串序列
# print
# str.join(seq);
# 以上实例输出结果如下：
#
# a - b - c


####    测试
sl = Solution()
s = "hello world"
print(sl.replaceSpace(s))