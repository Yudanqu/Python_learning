#!/usr/bin/env python
# -*- coding:utf-8 -*-

for row in range(1,10):
    for col in range(1,row+1):
        print('%d*%d=%d' %(col,row,row*col),end = ' ')
        # python3中默认print末尾换行，只要将end更改默认值为空或空格即可实现不自动换行
    print('\n')