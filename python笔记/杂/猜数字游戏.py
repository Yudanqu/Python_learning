#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
num = random.randint(1,100)
guess = 0
while True:
    num_guess = input('请输入一个1到100的数字：')
    guess += 1
    if not num_guess.isdigit():
        print('请输入数字')
        continue
    elif int(num_guess)<0 or int(num_guess)>100:
        print('输入数字应为1到100之间')
        continue
    else:
        if int(num_guess) < num:
            print('输入的值小于实际值，请重新输入：')
        elif int(num_guess) > num:
            print('输入的值大于实际值，请重新输入：')
        else:
            print('输入正确,正确的值为:%d,一共测试了%d次' %(int(num_guess),guess))
            break

print('随机值为：',num)