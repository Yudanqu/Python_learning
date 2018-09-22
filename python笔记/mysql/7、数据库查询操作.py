import pymysql

'''
fetchone()
功能：获取下一个查询结果集，结果集是一个对象

fetchall()
功能：接收全部的返回的行

rowcount
是一个只读属性，返回execute()方法影响的行数
'''

db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = "select * from bandcard where money>200"
try:
	cursor.execute(sql)

	reslist = cursor.fetchall()
	for row in reslist:
		print("%d--%d" % (row[0], row[1]))
except:
	# 如果提交失败，回滚到上一次数据
	db.rollback()
cursor.close()
db.close()
