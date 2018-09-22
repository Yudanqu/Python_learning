map():
map(func, lsd)
参数1是函数
参数2是序列

功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为一个新的Iterator返回

可迭代对象是个惰性的列表，直接输出为一个地址，要想输出里面内容要显示的写出来，eg：print(list(res))

def char2int(chr):
	return {'0':0, '1':1, '2':2, '3':3}[chr]

lis = ['2','1','3','0']
res = map(char2int, lis)
res2 = map(int, lis)
print(res)
print(list(res))
print(list(res2))
------------------------------------------------------------------------------------

reduce():
reduce(func, lsd)
参数1是函数
参数2是序列
注：reduce需要引入：from functools import reduce

功能：一个函数作用在序列上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素累积运算
eg: reduce(f, [a,b,c,d])
	f(f(f(a,b),c),d)

from functools import reduce

def Sum(a,b):
	return a + b
lis = [1,2,3,4,5]

res3 = reduce(Sum, lis)
print(res3)
-----------------------------------------------------------------------------------

map reduce 综合使用：

from functools import reduce

def str2int(str):
	def fc(x,y):
		return x * 10 + y
	def fs(chr):
		return {'0':0, '1':1, '2':2, '3':3,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[chr]
	return reduce(fc, map(fs,list(str)))
res4 = str2int('2314233123')
print(res4)