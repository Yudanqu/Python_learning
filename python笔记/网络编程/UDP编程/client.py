#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("请输入数据：")
    client.sendto(data.encode('utf-8'), ('192.168.1.235', 8082))
