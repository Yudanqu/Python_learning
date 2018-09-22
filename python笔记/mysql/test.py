from my_sql import my_sql

s = my_sql("192.168.19.1", "root", "123456", "student")

# 查询
res = s.get_all("select * from bandcard where money>200")
for row in res:
	print("%d--%d" % (row[0], row[1]))