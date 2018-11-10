'''
客户端：创建TCP连接时，主动发起连接的叫做客户端
服务端：接收客户端的连接
'''

import socket

# 创建一个socket
# 参数1：指定协议  socket.AF_INET 或  AF_INET6 （ipv4或ipv6）
# 参数2：SOCK_STREAM 执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
# address 为元组，第一个为地址，第二个为端口
sk.connect(("www.sina.com.cn",80))

sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 等待接收数据
data = []
while True:
	# 每次接收1k的数据
	tempData = sk.recv(1024)
	if tempData:
		data.append(tempData)
	else:
		break

datastr = (b''.join(data)).decode('utf-8')

# 断开连接
sk.close()
print(datastr)