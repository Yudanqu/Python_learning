#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = 3
b = 5
def func(a,b):
    c=a%b
    if c!=0:
        a=b
        b=c
        func(a,b)
    else:
        print(b)
func(a,b)