#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-06-21 11:38:17
# @Author  : yudanqu (943775910@qq.com)
# @Link    : https://www.cnblogs.com/yudanqu/
# @Version : $Id$


# 读取文件
f = open('xyj.txt', 'r', encoding="utf-8")

characters = []
stat = {}

for line in f:
	# 去掉每行两边的空白
	line = line.strip()
	# 如果该行为空行则跳过该轮循环
	if len(line) == 0:
		continue

	# 将文本转为Unicode，便于处理汉字
	# line = unicode(line)

	# 遍历该行的每一个字
	for x in range(0, len(line)):
		# 去掉标点符号和空白符
		if line[x] in [' ', '\t', '\n', '。', '，', '（', '）', '(', ')', '：', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		# 尚未在characters中
		if line[x] not in characters:
			characters.append(line[x])
		# 尚未记录在stat中
		# Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代:
		if not stat.__contains__(line[x]):
			stat[line[x]] = 0

		# 汉字出现次数加一
		stat[line[x]] += 1

print(len(characters))
print(len(stat))

# lambda生成一个临时函数
# d表示字典的每一对键值对，d[0]为key，d[1]为value
# reverse为True表示降序排序
stat = sorted(stat.items(), key=lambda d:d[1], reverse=True)

ff = open('result.csv', 'w')
for item in stat:
	# 进行字符串拼接之前，需要将int转为str
	ff.write(item[0] + ',' + str(item[1]) + '\n')
f.close()
ff.close()