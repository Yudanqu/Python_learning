可迭代对象：
    可以直接作用于for循环的对象统称为可迭代对象
（Iterable），可以用isinstance()去判断一个对象是否是可迭代对象

可以直接用于for的数据类型一般分为两种
1、结合数据类型，如list、tuple、dict、set、string
2、是generator，包括生成器和带yield的generator function
    from collections import Iterable
print(isinstance([], Iterable))  # 判断是否是可迭代对象

迭代器：
    不但可以作用于for循环，还可以被next()不断的调用并返回下一个值，知道最后抛出一个错误StopIteration错误表示无法继续返回下一个值

可以被next()函数调用并不断返回下一个值得对象称为迭代器
(Iterator对象)

可以使用isinstance()函数判断一个对象是否是Iterator对象
    from collections import Iterator
    print(isinstance((x for x in range(10)), Iterator))
    这个才是迭代器，上方的是可迭代对象，比如[](){}"", 这些都只是迭代对象

迭代器可以被next()调用：
    l = (x for x in range(5))
    print(next(l))
    print(next(l))

列表转迭代器：
    a = iter([1, 2, 3, 4])
    print(next(a))
    元组，字符串，字典都可以这样


案例：
    endstr = 'end'
    str = ""

    for line in iter(input, endstr):
        str += line + '\n'

    print(str)
    # 目的就是为了使input不直接退出，可以换行继续输入
