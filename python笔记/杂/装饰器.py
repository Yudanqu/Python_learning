'''
概念：是一个闭包，把一个函数当做参数返回一个替代版的函数，本质上就是一个返回函数的函数
'''

# 简单的装饰器


def func2(func):
    def inner():
        print('************')
        func()
    return inner


def func1():
    print("this is one")

f = func2(func1)
f()

# 装饰器进阶（含有一个参数）


def func4(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

'''
def func3(age):
	print("this is two %d" % age)

f = func4(func3)

f(-7)
'''
# 等效于上方代码


@func4
def func3(age):
    print("this is two %d" % age)
# 这时就可以直接使用原来的func3函数了，不需要引入变量来接收，就已经可以使用装饰器里的内容
func3(-7)
# 但此时的装饰器只能接收一个参数，为整形，因为内部使用了判断

# python2.4开始可以使用@符号


# 进进阶装饰器（通用装饰器）
def func5(func):
    def inner(*args, **kwargs):
        # 功能
        print("&&&&&&")
        func(*args, **kwargs)
    return inner


@func5
def func6(name, age, gender=1, number='00000000'):
    print('%s is %d years old,number is %s,gender:%d' %
          (name, age, number, gender))
func6('张三', 18, 0, '05162002')

# 函数的参数理论上是无限制的，但实际上最好不要超过6到7个
