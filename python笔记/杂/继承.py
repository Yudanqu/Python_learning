#!/usr/bin/env python
# -*- coding:utf-8 -*-

class father:
    def chi(self):
        print('chi....')
    def he(self):
        print('he....')
    def la(self):
        print('la....')
    def sa(self):
        print('sa....')

class son1(father):
    def mao(self):
        print('maiomiaojiao...')

class son2(father):
    def gou(self):
        print('wangwangjiao...')

obj1 = son1()
obj2 = son2()
obj1.chi()
obj2.gou()