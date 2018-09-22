def char2int(chr):
	return {'0':0, '1':1, '2':2, '3':3}[chr]

lis = ['2','1','3','0']
res = map(char2int, lis)
res2 = map(int, lis)
print(res)
print(list(res))
print(list(res2))

# *****************************************************************************

from functools import reduce

def Sum(a,b):
	return a + b
lis = [1,2,3,4,5]

res3 = reduce(Sum, lis)
print(res3)

# *****************************************************************************

def str2int(str):
	def fc(x,y):
		return x * 10 + y
	def fs(chr):
		return {'0':0, '1':1, '2':2, '3':3,'4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[chr]
	return reduce(fc, map(fs,list(str)))
res4 = str2int('2314233123')
print(res4)
print(int('2314233123'))

# *****************************************************************************

list1 = [1,2,3,4,5,6,7,8,9,0]
def func1(num):
	if num % 2 == 0:
		return True
	else:
		return False

res5 = filter(func1, list1)
print(res5) # 惰性列表，这样只输出地址
print(list(res5))

# *****************************************************************************

lis1 = [3,4,5,3,5,7,8,6,9]
lis2 = sorted(lis1)
print(lis1)
print(lis2)

# *****************************************************************************

lis3 = [3,4,-5,3,5,-7,8,6,9]
lis4 = sorted(lis3, key = abs)
print(lis3)
print(lis4)