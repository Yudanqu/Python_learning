import re

'''
1、字符串切割
'''

str1 = "hello world   hello world  hello world   "
# 普通切割
print(str1.split(' '))
# 正则切割
print(re.split(r' +', str1))



'''
2、re.finditer函数
原型：finditer(pattern, string, flags=0)
参数：
	pattern：匹配的正则表达式
	string：要匹配的字符串
	flags：标志位，用来控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
'''

str2 = "hello world hello world hello world hello world hello world"

d = re.finditer(r'hello', str2)
while True:
	try:
		print(next(d))
	except StopIteration as e:
		break


'''
3、字符串的替换和修改

sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern: 正则表达式（规则）
repl: 指定的用来替换的字符串
string: 目标字符串
count: 最多替换次数
flags:
功能： 在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。可以指定替换的次数，如果不指定，替换所有的匹配字符串
区别： sub返回一个字符串，subn返回一个元组（第一个元素是替换后的字符串，第二个元素是替换的个数）
'''
# re.sub(pattern, repl, string)


'''
4、分组

概念：除了简单的判断是否匹配以外，正则表达式还有提取子串的功能。用()表示的就是提取分组

'''

str3 = "010-12312323"
m = re.match(r'(?P<first>\d{3})-(\d{8})', str3)
# 使用序号获取对应组的信息，group(0)一直代表的原始字符串
print(m.group(0))
print(m.group(1))
print(m.group('first'))
print(m.group(2))

# 查看各组的情况
print(m.groups())

# 如果在最外层加一个括号，那么group(1)就是打印的最外面的那个，依次向里

# ?P<first>写在小括号里，表示起名字


'''
5、编译: 当我们使用正则表达式时，re模块会干两件事
	1、编译正则表达式，如果正则表达式本身不合法，会报错
	2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
'''

# 一般正则对象称其为re_xxxx
pat = r"^1(([3578]\d)|(47))\d{8}$"
re_telephone = re.compile(pat)
print(re_telephone.match("13612345678"))