#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo:

    def __init__(self,name,age,sex,capacity):
        self.name = name
        self.age = age
        self.sex = sex
        self.capacity = capacity

    #内容
    def caocongzhandou(self):
        print('%s 参加草丛战斗，消耗200战力' %self.name)
        self.capacity -= 200

    def ziwoxiulian(self):
        print('%s 进行自我修炼，增长100战力' %self.name)
        self.capacity += 100

    def duorenyouxi(self):
        print('%s 参加多人游戏，消耗500战力' %self.name)
        self.capacity -= 500

    def detail(self):
        print('%s,%d岁,%s,剩余%d战力' %(self.name,self.age,self.sex,self.capacity))

#初始化任务状态
obj1 = Foo('小一',5,'男',1000)
obj2 = Foo('小二',6,'男',1800)
obj3 = Foo('小四',7,'女',2500)

#过程
obj1.ziwoxiulian()
obj1.ziwoxiulian()
obj2.caocongzhandou()
obj3.duorenyouxi()

#输出状态
obj1.detail()
obj2.detail()
obj3.detail()