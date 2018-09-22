#!/usr/bin/env python
# -*- coding:utf-8 -*-

def func(n):
    if n == 1:
        return 1
    return func(n-1) * n

res = func(5)
print('5以内累乘得：%d' % res)