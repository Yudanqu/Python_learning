#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

class Admin(object):
    admin = "1"
    passwd = "1"

    def printAdminView(self):
        print("****************************************************")
        print("*                                                  *")
        print("*                                                  *")
        print("*               欢迎登陆银行                       *")
        print("*                                                  *")
        print("*                                                  *")
        print("****************************************************")

    def printSysFunctionView(self):
        print("****************************************************")
        print("*         开户（1）            查询（2）            *")
        print("*         取款（3）            存款（4）            *")
        print("*         转账（5）            改密（6）            *")
        print("*         锁定（7）            解锁（8）            *")
        print("*         补卡（9）            销户（0）            *")
        print("*                    退出（q）                     *")
        print("****************************************************")

    def adminOption(self):
        inputAdmin = input("请输入管理员账号：")
        if self.admin != inputAdmin:
            print("输入账号有误！")
            return -1
        inputPasswd = input("请输入管理员密码：")
        if self.passwd != inputPasswd:
            print("密码输入有误！")
            return -1

        # 能执行到这里说明账号密码正确
        print("操作成功，请稍后······")
        time.sleep(2)
        return 0

    def ban(self, allUsers):
        for key in allUsers:
            print("账号：" + key + "\n" + "姓名:" + allUsers[key].name + "\n" + "身份证号：" + allUsers[key].idCard + "\n" + "电话号码：" + allUsers[
                key].phone + "\n" + "银行卡密码：" + allUsers[key].card.cardPasswd + "\n")
