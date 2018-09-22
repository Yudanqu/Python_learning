什么是柯里化？
	原来接受两个参数的函数变成接受一个参数的函数的过程。（多个同理）
	新的参数返回一个以原有第二参数为参数的函数
	z = f(x, y) ---> z = f(x)(y)

eg:x + y 柯里化
**********************
def add(x,y):
	return x + y

print(add(4, 5))
*********************
def new_add(x):
	def inner(y):
		return x + y
	return inner

foo = new_add(4)
foo(5)

print(new_add(4)(5))
*********************

def logger(fn):
	def inner(*args, **kwargs):
		ret = fn(*args, **kwargs)
		return ret
	return inner

@logger
def add(x, y):
	return x + y

# add = logger(add)
print(add(4,5))