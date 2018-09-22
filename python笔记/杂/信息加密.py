#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = 'cagy'
c = []
b = 3
for var in a:
    if ord(var)+b > ord('z'):#ord是将字符转换为ascii码
        num = ord(var)+b-26
    else:
        num = ord(var)+b
    c.append(chr(num))#chr是将ascii码转换为字符
print(''.join(c))
