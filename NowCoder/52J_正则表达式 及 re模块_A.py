#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/29


#正则表达式 及 re模块
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        import re
        # 返回所有s中符合正则式pattern的字符串 k为list
        k = re.findall(pattern, s)
        if s in k:
            return True
        else:
            return False

if __name__ == '__main__':
    s = 'aaa'
    pattern = "ab*ac*a"
    a = Solution()
    print(a.match(s,pattern))