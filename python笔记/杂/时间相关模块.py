'''
time
'''

'''
UTC(世界协调时间)：格林尼治天文时间，世界标准时间，在中国来说是UTC+8
DST(夏令时)：是一种节约能源而认为规定时间制度，在夏季调快一小时


时间的表示形式：
1、时间戳
	以整型或浮点型表示时间的一个以秒为单位的时间间隔，这个时间间隔，这个时间间隔的基础值是从1970年1月1日0点开始算起

2、元组
	一种python的数据结构表示，这个元组有9个整型内容
	year
	month
	day
	hours
	minutes
	seconds
	weekday
	Julia day
	flag (1 或 -1 或 0)
3、格式化字符串

'''


import time

# 返回当前时间的时间戳，浮点数形式，不需要参数
c = time.time()
print(c)

# 将时间戳转为UTC时间元组（格林尼治时间）
t = time.gmtime(c)

# 将时间戳转为本地时间元组
b = time.localtime(c)

# 将本地时间（元组）转为时间戳
m = time.mktime(b)  # 后面的小数省略了

# 将时间元组转成字符串
s = time.asctime(b)

# 将时间戳转为字符串
p = time.ctime(c)

# 将时间元组转换成指定格式的字符串
q = time.strftime("%Y-%m-%d %H:%M:%S", b)
# 第二个参数可以不写，不写就是默认转当前时间，写了就是转需要转的时间

# 将时间字符串转换成时间元组
w = time.strptime(q, "%Y-%m-%d %X")


# 延迟一个时间，整型或浮点型
time.sleep(6)

# 返回当前程序的cpu执行时间
# Unix始终返回全部的运行时间
# Windows从第二次开始，都是以第一个调用次函数的开始时间戳做完基数
y1 = time.clock()
print(y1)
time.sleep(1)
y22 = time.clock()
print(y2)
# 与第一次的时间戳的差值


# 性能测试
import time
time.clock()
sum = 0
for i in range(100000000):
    sum += i
print(time.clock())


'''
datetime比time高级了不少，可以理解为datetime基于time进行封装，提供了各种使用的函数，datetime模块的接口更直观，更容易调用


模块中的类：
datetime：同时有时间和日期
timedelta：主要用于计算时间的跨度
tzinfo：时区相关
time：只关注时间
date：只关注日期

'''


import datetime

# 获取当前时间
d1 = datetime.datetime.now()

# 获取指定时间
d2 = datetime.datetime(1999, 10, 1, 10, 28, 25, 123456)

# 将时间转为字符串
d3 = d1.strftime("%y-%m-%d %X")

# 将格式化字符串转为datetime对象
d4 = datetime.datetime.strptime(d3, "%y-%m-%d %X")  # 格式得对应

# d1,d2那样的可以加减
eg：d5 = d2 - d1
print(d5.days)  # 输出间隔的天数
print(d5.seconds)  # 间隔天数除外的秒数


'''
calendar:日历模块
'''
import calendar

# 使用

# 返回某年某月的日历
print(calendar.month(2017, 7))

# 返回某年的日历
print(calendar.calendar(2017))

# 判断是否为闰年，是则返回True
print(calendar.isleap(2000))

# 返回某个月weekday的第一天，和这个月一共的天数
print(calendar.monthrange(2017, 7))

# 返回某个月以每周为元素的列表
print(calendar.monthcalendar(2017, 7))
