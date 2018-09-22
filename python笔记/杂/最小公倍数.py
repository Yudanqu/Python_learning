#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = 3
b = 5
x = a*b
def func(a,b,x):
    c=a%b
    if c!=0:
        a=b
        b=c
        func(a,b,x)
    else:
        print(x//b)
func(a,b,x)