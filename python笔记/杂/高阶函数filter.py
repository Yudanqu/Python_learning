
过滤器：

filter(function or None, iterable)
参数一：函数
参数二：序列

功能：用于过滤序列，把传入的函数依次作用于序列的每一个函数根据返回的是True和False决定是否保留该元素


list1 = [1,2,3,4,5,6,7,8,9,0]
def func1(num):
	if num % 2 == 0:
		return True
	else:
		return False

res5 = filter(func1, list1)
print(res5) # 惰性列表，这样只输出地址
print(list(res5))