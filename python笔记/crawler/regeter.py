fp = open('密码','a+')#读写兼备
while True:
	account = input('请输入你的账号：')
	fp.seek(0,0)#移动读写指针
	for buf in fp:
		file_account = buf.aplit(':')[0]
		if file_account == account:
			print('已经被注册，请重新输入！')
			is_register = True
			break
	if not is_register:
		passwd = input('请输入你的密码：')
		new_str = account + ':' + passwd +'\n'
		fp.write(new_str)
		print('注册成功')	
		break
	else:
		continue
fp.close()