import pymysql


db = pymysql.connect("localhost", "root", "123456", "student")
cursor = db.cursor()

# 检查表是否存在，如果有则删除
cursor.execute("drop table if exists bancard")

# 建表
sql = "create table bandcard(id int auto_increment primary key, money int not null)"
cursor.execute(sql)

cursor.close()
db.close()
