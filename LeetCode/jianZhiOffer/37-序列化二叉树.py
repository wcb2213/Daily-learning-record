#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/23


class Solution:
    def Serialize(self, root):
        # write code here
        if not root: return '#,'
        s=''
        queue=[root]
        while queue:
            for i in queue:
                if i: s+=str(i.val)+','
                else: s+='#,'
            tmp=[]
            for i in queue:
                if i.left: tmp.append(i.left)
                if i.right: tmp.append(i.right)
            queue=tmp
        return s
    def Deserialize(self, s):
        # write code here
        if s=='#,': return None
        l=s[:-1].split(',')
        root=TreeNode(int(l[0]))
        queue=[root]
        i=1
        while queue:
            p=queue.pop(0)
            if l[i]!='#':
                p.left=TreeNode(int(l[i]))
                queue.append(p.left)
            i+=1
            if l[i]!='#':
                p.right=TreeNode(int(l[i]))
                queue.append(p.right)
            i+=1
        return root