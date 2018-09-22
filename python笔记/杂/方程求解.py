#!/usr/bin/env python
# -*- coding:utf-8 -*-

def quadratic(a,b,c):
    for x in range(-100,100):#如何表示全体实数
        if a*x**2 + b*x + c == 0:
            print('方程的解是：%d' % x)

quadratic(1,3,2)