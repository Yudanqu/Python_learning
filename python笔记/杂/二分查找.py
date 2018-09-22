#!/usr/bin/env python
# -*- coding:utf-8 -*-

def binary_search(data,find_n):
    if len(data) > 1:
        mid = int(len(data)/2)
        if data[mid] > find_n:
            print("data in left of %s" % data[mid])
            binary_search(data[:mid],find_n)
        elif data[mid] < find_n:
            print("data in right of %s" % data[mid])
            binary_search(data[mid:],find_n)
        else:
            print("found find_n,",data[mid])
    else:
        print("can't found ……")

if __name__ == '__main__':
    data = list(range(1,600,4))
    binary_search(data,357)