#!/usr/bin/env python
# -*- coding:utf-8 -*-
from user import User
from card import Card
import random
import time

class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers # 用户字典

    # 开户
    def creatUser(self):
        # 目标：向用户字典中添加一对键值对（卡号->用户）
        name = input("请输入您的名字：")
        idCard = input("请输入您的身份证号：")
        phone = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("预存款输入有误！开户失败")
            return -1

        onePasswd = input("请设置密码：")
        # 验证密码
        if not self.checkPasswd(onePasswd):
            print("输入密码错误，开户失败！")
            return -1

        # 生成银行卡号
        cardStr = self.randomCardId()
        card = Card(cardStr, onePasswd, prestoreMoney)

        user = User(name, idCard, phone, card)
        # 存到字典
        self.allUsers[cardStr] = user
        print("开户成功！请记住卡号：" + cardStr)

    # 查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，查询失败！")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，该卡已锁定！请解锁后再使用其功能！")
            user.card.cardLock = True
            return -1
        print("账号：%s   余额：%d" % (user.card.cardId, user.card.cardMony))

    # 取款
    def getMoney(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，取款失败！")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，该卡已锁定！请解锁后再使用其功能！")
            user.card.cardLock = True
            return -1

        # 开始取款
        amount = int(input("验证成功！请输入取款金额："))
        if amount > user.card.cardMony:
            print("取款金额有误，取款失败！")
            return -1
        if amount < 0:
            print("取款金额有误，取款失败！")
            return -1
        user.card.cardMony -= amount
        print("您取款%d元，余额为%d元！" % (amount, user.card.cardMony))

    # 存款
    def saveMoney(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，存款失败！")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，该卡已锁定！请解锁后再使用其功能！")
            user.card.cardLock = True
            return -1

        # 开始存款
        amount = int(input("验证成功！请输入存款金额："))
        if amount < 0:
            print("存款金额有误，存款失败！")
            return -1
        user.card.cardMony += amount
        print("您存款%d元，最新余额为%d元！" % (amount, user.card.cardMony))

    # 转账
    def transferMoney(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，转账失败！")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，该卡已锁定！请解锁后再使用其功能！")
            user.card.cardLock = True
            return -1

        # 开始转账
        amount = int(input("验证成功！请输入转账金额："))
        if amount > user.card.cardMony or amount < 0:
            print("金额有误，转账失败！")
            return -1

        newcard = input("请输入转入账户：")
        newuser = self.allUsers.get(newcard)
        if not newuser:
            print("该卡号不存在，转账失败！")
            return -1
        # 判断是否锁定
        if newuser.card.cardLock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1
        user.card.cardMony -= amount
        newuser.card.cardMony += amount
        time.sleep(1)
        print("转账成功，请稍后···")
        time.sleep(1)
        print("转账金额%d元，余额为%d元！" % (amount, user.card.cardMony))

    # 改密
    def changePasswd(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，改密失败！")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，该卡已锁定！请解锁后再使用其功能！")
            user.card.cardLock = True
            return -1
        print("正在验证，请稍等···")
        time.sleep(1)
        print("验证成功！")
        time.sleep(1)

        # 开始改密
        newPasswd = input("请输入新密码：")
        if not self.checkPasswd(newPasswd):
            print("密码错误，改密失败！")
            return -1
        user.card.cardPasswd = newPasswd
        print("改密成功！请稍后！")

    # 锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，锁定失败！")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定，请解锁后再使用其功能！")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，锁定失败！")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号输入有误，锁定失败！")
            return -1
        # 锁定
        user.card.cardLock = True
        print("锁定成功！")


    # 解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，解锁失败！")
            return -1
        if not user.card.cardLock:
            print("该卡未被锁定，无需解锁！")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，解锁失败！")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证号输入有误，解锁失败！")
            return -1
        # 解锁
        user.card.cardLock = False
        print("解锁成功！")

    # 补卡
    def newCard(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！")
            return -1
        tempname = input("请输入您的姓名：")
        tempidcard = input("请输入您的身份证号码：")
        tempphone = input("请输入您的手机号码：")
        if tempname != self.allUsers[cardNum].name\
                or tempidcard != self.allUsers.idCard\
                or tempphone != self.allUsers.phone:
            print("信息有误，补卡失败！")
            return -1
        newPasswd = input("请输入您的新密码：")
        if not self.checkPasswd(newPasswd):
            print("密码错误，补卡失败！")
            return -1
        self.allUsers.card.cardPasswd = newPasswd
        time.sleep(1)
        print("补卡成功，请牢记您的新密码！")

    # 销户
    def killUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在，转账失败！")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已锁定！请解锁后再使用其功能！")
            return -1

        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误，该卡已锁定！请解锁后再使用其功能！")
            user.card.cardLock = True
            return -1

        del self.allUsers[cardNum]
        time.sleep(1)
        print("销户成功，请稍后！")

    # 验证密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    # 生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord("0"), ord("9") + 1))
                str += ch
            # 判断是否重复
            if not self.allUsers.get(str):
                return str
