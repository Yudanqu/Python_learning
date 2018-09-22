#!/usr/bin/env python
# -*- coding:utf-8 -*-

L = [2,8,3,50,]
def func(x):
    if x % 10 == 0:
        x = x // 10
    #else:
    #    pass
    #注释掉的在pycharm运行成功，在线编译失败
    return x
length = len(L)
for i in range(0,length-1):
    L[i+1] = L[i]*L[i+1]
    L[i+1] = func(L[i+1])
print(L[i]%2)