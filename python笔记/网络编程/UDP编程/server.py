#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

udpServe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpServe.bind(('192.168.1.235', 8082))

while True:
    data, addr = udpServe.recvfrom(1024)
    print("客户端说：", data.decode('utf-8'))
