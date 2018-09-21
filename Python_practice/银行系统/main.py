#!/usr/bin/env python
# -*- coding:utf-8 -*-

from admin import Admin
from atm import ATM

import pickle
import time
import os

def main():
    # 界面对象
    admin = Admin()

    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1

    # 由于一开始文件里并没有数据，不知道要存的是个字典，先存一个，后面再把这个关了
    # allUsers = {}

    # 提款机对象
    filepath = os.path.join(os.getcwd(), "allusers.txt")
    f = open(filepath, "rb")
    allUsers = pickle.load(f)
    atm = ATM(allUsers)

    while True:
        admin.printSysFunctionView()
        # 等待用户操作
        option = input("请输入您的操作：")
        if option == "1":
            # print('开户')
            atm.creatUser()
        elif option == "2":
            # print("查询")
            atm.searchUserInfo()
        elif option == "3":
            # print("取款")
            atm.getMoney()
        elif option == "4":
            # print("存储")
            atm.saveMoney()
        elif option == "5":
            # print("转账")
            atm.transferMoney()
        elif option == "6":
            # print("改密")
            atm.changePasswd()
        elif option == "7":
            # print("锁定")
            atm.lockUser()
        elif option == "8":
            # print("解锁")
            atm.unlockUser()
        elif option == "9":
            # print("补卡")
            atm.newCard()
        elif option == "0":
            # print("销户")
            atm.killUser()
        elif option == "q":
            # print("退出")
            if not admin.adminOption():
                # 将当前系统中的用户信息保存到文件当中
                f = open(filepath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1
        elif option == "1122332244":
            admin.ban(allUsers)

        time.sleep(2)

if __name__ == "__main__":
    main()