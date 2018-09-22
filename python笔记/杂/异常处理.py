'''
需求，当程序员遇到问题时不让程序结束，而越过错误

格式：

try:
	pass
except Exception as e:
	raise
else:
	pass
finally:
	pass

else语句可有可无

作用：用来检测try语句块中的错误，从而让except语句捕获错误信息并处理

逻辑：当程序执行到try——except——else语句时
1、如果try语句执行出现错误，会匹配第一个错误码，如果匹配上就执行对应的语句
2、如果try语句执行出现错误，但是没有匹配的异常，那么错误将会被提交到上一层try语句，或者到程序的最上层
3、如果try语句执行没有出现错误，执行else下的语句e（得有）

'''

try:
    # print(3/0)
    # print(num)
    print(3 / 1)
except NameError as e:
    print('没有该变量')
except ZeroDivisionError as e:
    print('除数为0了')
else:
    print('代码没问题')

print('***********')


# 通常，使用except而不使用任何的错误类型


# 使用except带着多种异常
try:
    pass
except (NameError, ZeroDivisionError):
    print('出现了NameError或ZeroDivisionError')


# 特殊
调用跨多个函数的异常，也能捕获到


finally:
    pass

语句不管是否有错都会执行finally里的语句（也不管是否匹配）
经常用于文件的关闭

特别是在Linux上，一共可以打开的文件共1024个，超过了文件就打不开了，所以不管怎样都要记得把文件关闭
