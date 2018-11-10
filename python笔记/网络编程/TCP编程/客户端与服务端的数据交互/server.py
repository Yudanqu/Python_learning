#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口
sever.bind(('192.168.1.235', 8081))  # 一般不要用1024以下的
# 监听
sever.listen(5)

print("服务器启动成功！")

# 等待连接
clientSocket, clientAddress = sever.accept()

print("%s -- %s 连接成功" % (str(clientSocket), clientAddress))
while True:
    data = clientSocket.recv(1024)
    print("收到" + str(clientSocket) + "的数据：" + data.decode("utf-8"))
    clientSocket.send("very good...".encode("utf-8"))
