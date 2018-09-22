#!/usr/bin/env python
# -*- coding:utf-8 -*-

L = [2,8,3,50]
num = 0
length = len(L)
for i in range(0,length-1):
    L[i+1] = L[i]*L[i+1]
    if L[i+1]%10==0:
        num = num + 1
        L[i+1] = L[i+1]//10
        if L[i+1]%10==0:
            num = num + 1
            L[i + 1] = L[i + 1] // 10
        else:
            pass
    else:
        pass
print(num)