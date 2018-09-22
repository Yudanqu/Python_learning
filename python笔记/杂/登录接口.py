# python 3.6 登录接口练习
# _*_ coding:utf-8 _*_
import sys
import os
import getpass

i = 0
while i < 3:
    username = input("请输入用户名：")
    with open("account_lock.txt", "r") as account_lock_file:  # 打开锁定用户文件，r为只读
        account_lock_list = account_lock_file.readlines()  # 转换成列表

    for lock_name in account_lock_list:  # 循环遍历文件
        lock_name = lock_name.strip('\n')  # 去掉换行符
        if username == lock_name:
            sys.exit("用户{_username}已被锁定，请联系管理员解锁！！".format(_username=username))

    #password =input("请输入密码：")
    with open("accounts.txt", 'r') as account_file:
        account_list = account_file.readlines()
    for account_line in account_list:
        (name, pas) = account_line.strip('\n').split()  # 去掉换行符，并以，为切片

        if username == name:
            j = 0
            while j < 3:
                password = getpass.getpass("请输入用户密码：")
                if password == pas:
                    print("用户{_name}登录成功".format(_name=username))
                    sys.exit()
                else:
                    if j != 2:
                        print("用户{_name}密码输入错误，请重新输入，还有{d}次机会".format(
                            _name=username, d=2 - j))
                j = j + 1
            else:
                with open("account_lock.txt", 'a+') as account_lock_file:
                    account_lock_file.write(username + '\n')
                    sys.exit("超过最大错误次数，用户{_name}已被锁定，并退出".format(
                        _name=username))
        else:
            pass
    else:
        if i != 2:
            print("用户{_name}不存在，请重新输入，还有{d}次机会！".format(
                _name=username, d=2 - i))
    i = i + 1  # 当用户输入用户名错误时增加错误次数
else:
    sys.exit("用户{_username}不存在，系统即将退出".format(_username=username))
