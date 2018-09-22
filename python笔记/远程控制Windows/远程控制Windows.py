import telnetlib

def telnetdosomething(IP, user, passwd, command):
	
	try:
		# 连接服务器
		telnet = telnetlib.Telnet(IP)
		# 设置调试级别
		telnet.set_debuglevel(2)

		# 读取输入用户名信息
		rt = telnet.read_until("Login username:".encode("utf-8"))
		# 写入用户名
		telnet.write((user+"\r\n").encode("utf-8")) # windows中的回车

		# 读取输入密码信息
		rt = telnet.read_until("Login password:".encode("utf-8"))
		# 写入密码
		telnet.write((passwd+"\r\n").encode("utf-8")) # windows中的回车

		# 读取验证信息
		rt = telnet.read_until("Domain name:".encode("utf-8"))
		# 写入验证信息
		telnet.write((IP+"\r\n").encode("utf-8")) # windows中的回车

		# 登陆成功，写指令
		rt = telnet.read_until(">".encode("utf-8"))
		# 写入指令
		telnet.write((command+"\r\n").encode("utf-8")) # windows中的回车

		# 上面命令执行成功会继续读到>，失败一般不会出现>
		rt = telnet.read_until(">".encode("utf-8"))

		# 断开连接
		telnet.close()
		return True
	except:
		return False

if __name__ == "__main__":
	IP = "10.0.142.197"
	user = "xumingbin"
	passwd = "1103"
	command = "tasklist"
	telnetdosomething(IP, user, passwd, command)