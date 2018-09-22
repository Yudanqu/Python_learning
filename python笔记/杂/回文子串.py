#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = 'assa'
a = list(a)
n = 3
flag = 2
for start in range(len(a)):
    new_a = a[start:start+n]
    #if new_a == reversed(new_a):
    nnew_a = [new_a,reversed==True]
    if new_a == nnew_a:
        flag = 1
        break
    else:
        flag = 0
        continue
print(new_a)
print(nnew_a)
if flag == 1:
    print('YES')
elif flag == 0:
    print('NO')
else:
    print('ononon')