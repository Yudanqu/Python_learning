#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.request import *
#用来处理网络访问
import re

url = 'http://image.baidu.com/search/index?word=dog&ct=201326592&cl=2&nc=1&lm=-1&st=-1&tn=baiduimage&istype=2&fm=index&pv=&z=0&ie=utf-8'

#用来打开一个网页并返回信息
html = urlopen(url)
#html代码
#获取html代码并解码
obj = html.read().decode()#解码前是二进制types
urls = re.findall(r'"objURL":"(.*?)"',obj)#?此时表示非贪婪
#print(urls)
index = 0
for url in urls:
    try:
        print('downloading....%d' % index)
        urlretrieve(url,'pic' + str(index) + '.jpg')
        #相对路径保存
        index += 1
    except Exception:
        print('download error....%d' % index)
    else:
        print('download complete....')