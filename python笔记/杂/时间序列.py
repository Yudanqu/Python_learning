import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from datetime import datetime

#时间序列数据的基础操作
t1 = datetime(2009,10,29)
date_list = [
	datetime(2015,3,5),
	datetime(2015,3,10),
	datetime(2017,2,20),
	datetime(2017,4,12)
]
s1 = Series(np.random.rand(4),index=date_list)
'''
返回数据的方式：
	1、根据索引号，0到3
	2、根据index，eg:datetime(2017,4,12)
	3、自己输入index，eg:'2017-4-12'(以时间的显示格式)或'20170412'(补全数位)
	想找到某范围的数据，可以用'2017' '2017-4'等等
'''
date_list_new = pd.date_range('2016-01-01',periods=100) #根据date_range函数来生成
#其中参数：前三个为起始、终止、间隔时间，间隔为periods，freq是指步长，'D'表示天，'W'表示周，其中'W-MON'即为更改周的哪一天为起始。



#对时间序列数据的采样和画图
t_range = pd.date_range('2017-01-01','2017-12-31')
s2 = Series(np.random.randn(len(t_range)),index=t_range) # 按天创建的数据，采样为每个月一个数据点
# s2['2017-01'].mean() 可以计算着一个月的平均值
s2_month = s2.resample('M').mean() #对s2按月采样，并求平均，最后这个求平均就是进行处理的方法，可以自己定义
s2_hour = s2.resample('H').ffill() #填充数据以小时，向后填充，就是以当前的数据向后面的小时填充
s2_hour = s2.resample('H').bfill() #向前填充，就是用下一天开头的数据填充前一天每小时
#画图
import matplotlib.pyplot as plt
t_range = pd.date_range('2017-01-01','2017-12-31',freq='H')
stock_df = DataFrame(index=t_range)
stock_df['aaa'] = np.random.randint(80,160,size=len(t_range))
stock_df['bbb'] = np.random.randint(30,50,size=len(t_range))
stock_df.plot()
plt.show() #有图像，但是不容易观察，所以要用上面学到的数据采样来调整

week_df = DataFrame()
week_df['aaa'] = stock_df['aaa'].resample('W').mean()
week_df['bbb'] = stock_df['bbb'].resample('W').mean()
week_df.plot()
plt.show()