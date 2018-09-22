#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Person(object):
    # 这里的属性实际上不是对象属性，是类属性(用类名来调用)
    name = "person"

    def __init__(self,name):
        # 对象属性
        self.name = name


print(Person.name)

per = Person('tom')
print(per.name)
per.age = 19
print(per.age)
# 对象属性的优先级高于类属性
# 若没有此对象属性还可以动态的添加对象属性，仅对自己当前有效

del per.name
print(per.name)
# 删除了对象属性，但这时同名类属性还有，则自动调用类属性

# 注意：以后不要将对象属性和类属性重名，因为对象属性可以屏蔽同名的类属性，在删掉对象属性的时候，类属性又可以看到了
