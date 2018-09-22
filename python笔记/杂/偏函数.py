print(int('1010', base=2))
# base = 2 意思是把字符串当做二进制来计算


def int2(str, base=2):  # 表示设置默认值为2.将来用base值来转换
    return int(str, base)

可以通过控制参数来实现功能就是偏函数

import functools  # 这个模块帮我们定义偏函数

# 把一个参数固定住，形成一个新的函数
int2 = functools.partial(int, base=2)
# 和上面手写的一样
