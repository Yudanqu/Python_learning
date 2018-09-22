
python自1.5以后增加了re模块，提供了正则表达式模式

re模块使python语言拥有了全部的正则表达式功能


import re


re.match函数
原型：match(pattern, string, flags=0)
参数：
	pattern：匹配的正则表达式
	string：要匹配的字符串
	flags：标志位，用来控制正则表达式的匹配方式
		re.I：忽略大小写
		re.L：做本地化识别
		re.M：多行匹配，影响^和$
		re.S：使.匹配包括换行符在内的所有字符，否则.不匹配换行符
		re.U：根据Unicode字符集解析字符，影响'\w \W \b \B'
		re.X：使我们以更灵活的格式理解正则表达式
功能：尝试从字符串的起始位置匹配一个模式

print(re.match('www', 'www.baidu.com'))  # <_sre.SRE_Match object; span=(0, 3), match='www'>
print(re.match('www', 'www.baidu.com').span())  # (0, 3) 但会位置


re.search函数
原型：search(pattern, string, flags=0)
参数：
	pattern：匹配的正则表达式
	string：要匹配的字符串
	flags：标志位，用来控制正则表达式的匹配方式
功能：扫描整个字符串，返回第一个成功的匹配


re.findall函数
原型：findall(pattern, string, flags=0)
参数：
	pattern：匹配的正则表达式
	string：要匹配的字符串
	flags：标志位，用来控制正则表达式的匹配方式
功能：扫描整个字符串，返回结果列表