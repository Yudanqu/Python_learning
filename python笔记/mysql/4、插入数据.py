import pymysql


db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = "insert into bandcard values(0, 300)"
try:
	cursor.execute(sql)
	db.commit() # 执行这条才插入
except:
	# 如果提交失败，回滚到上一次数据
	db.rollback()
cursor.close()
db.close()
