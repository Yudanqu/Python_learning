#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


#m = re.match(pattern,data_source)

print(re.search('hello','hello world hello').span())
print(re.search('hello','hello world hello').group())
print(re.search('hello','hello world'))
print(re.search('worldf','hello world'))
