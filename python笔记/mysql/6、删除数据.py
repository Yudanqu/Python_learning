import pymysql


db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

sql = "delete from bandcard where money=200"
try:
	cursor.execute(sql)
	db.commit()
except:
	# 如果提交失败，回滚到上一次数据
	db.rollback()
cursor.close()
db.close()
