#!/usr/bin/env python
# -*- coding:utf-8 -*-

def ccount():
    fs = []
    for i in range(1,3):
        def f():
            return i*i
        fs.append(f)
        print(i)
        print(fs)
    return fs

f1,f2 = ccount()

print('f1=',f1())
print('f2=',f2())
#print('f3=',f3())
