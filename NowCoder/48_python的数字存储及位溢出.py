#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


# step1:按位与是查看两个数哪些二进制位都为1，这些都是进位位，结果需左移一位，表示进位后的结果
# step2:异或是查看两个数哪些二进制位只有一个为1，这些是非进位位，可以直接加、减，结果表示非进位位进行加操作后的结果
# step3:n1&n2是查看有没有进位位了，如果有，需要重复step1、step2；如果没有，保留n1、n2上二进制为1的部分，用或将之合为一个数，即为最后结果
class Solution:
    # ## 思路 但会溢出
    # def add(self, a: int, b: int) -> int:
    #     if b==0: return a
    #     return self.add(a^b,(a&b)<<1)
    def Add(self, num1, num2):
        # write code here
        x=0xffffffff
        while num2!=0:
            carry=num1&num2
            num1=(num1^num2)&x
            num2=(carry<<1)&x
        return num1 if num1<=0x7FFFFFFF else ~(num1 ^ x)
# Python 负数的存储：
# Python / Java 中的数字都是以 补码 形式存储的。但 Python 没有 int , long 等不同长度变量，即没有变量位数的概念。

# 获取负数的补码： 需要将数字与十六进制数 0xffffffff 相与。
# 可理解为舍去此数字 32 位以上的数字（1），从无限长度变为一个 32 位整数。

# 计算完成后还原成补码： 若补码 a 为负数（ 0x7fffffff 是最大的正数的补码 ），^ 异或
# 需执行 ~(a ^ x) 操作， ~(a ^ x) 是将 32 位以上的位取反，即由 0 变为 1 ， 1 至 32 位不变。
