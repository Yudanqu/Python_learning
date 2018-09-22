#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 导入发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText

# SMTP服务器
SMTPServer = "smtp.163.com"

# 发邮件的地址
Sender = "xxxxxxxxxx@163.com"
# 发送者邮箱的密码
passwd = "xxxxxxxxxxxxxxxx" # 授权密码，不能作为登录，仅能发



# 设置发送的内容
message = "my name is Chen"
# 转换成邮件文本
msg = MIMEText(message)

# 标题
msg["Subject"] = "来自远方的问候"

# 收件人
msg["From"] = Sender

# 创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25) # 25是端口号，一般是邮件用的
# 登录邮箱
mailServer.login(Sender,passwd)
# 发送邮件
mailServer.sendmail(Sender,["xxxxxxxxxxx@163.com","目标邮箱"],msg.as_string())
# 退出邮箱
mailServer.quit()


# 554错误
# 有时候是因为发送内容或标题不合法
# 或者账号不合法