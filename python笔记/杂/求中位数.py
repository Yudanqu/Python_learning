#!/usr/bin/env python
# -*- coding:utf-8 -*-

L = [0,1,2,3,4]
L.sort()
length = len(L)
if length%2 == 1:
    print(L[length//2])
else:
    x = (L[length//2-1]+L[length//2])*0.5
    print('%.1f' % x)