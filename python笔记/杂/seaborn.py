import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
import seaborn as sns

'''
直方图，密度图
'''
# 通过matplotlib画
s1 = Series(np.random.randn(1000))
plt.hist(s1) # 直方图
s1.plot(kind='kde') # 密度图

# 通过seaborn画
sns.distplot(s1,hist=True,kde=True,rug=True) # 前两个默认就是True,rug是在最下方显示出频率情况，默认为False
# bins=20 表示等分为20份的效果，同样有label等等参数
sns.kdeplot(s1,shade=True,color='r') # shade表示线下颜色为阴影,color表示下面是红色
sns.plt.plot(s1) # 此时和matplotlib一样
sns.plt.hist(s1) # 直方图 所以seaborn也可以直接调用matplotlib的函数
sns.rugplot(s1)


'''
柱状图，热力图
'''
df = sns.load_dataset('flights') # 在线下载一个数据用于实验
df = df.pivot(index='month',columns='year',values='passengers') # 生成一个透视表
sns.heatmap(df) # 生成热力图
# sns.heatmap(df,annot=True,fmt='d') # annot参数是指显示数据，fmt='d'是指以整数形式显示
df.plot() # 线性的显示数据情况

s = df.sum()
sns.barplot(x=s.index,y=s.values)

s.plot(kind='bar')


'''
seaborn设置图形显示效果
'''
1、axes_style and set_style
x = np.linspace(0,14,100)
y1 = np.sin(x)
y2 = np.sin(x+2)*1.25
def sinplot():
	plt.plot(x,y1)
	plt.plot(x,y2)

sinplot() # 以matplotlib显示
# seaborn的5种装饰风格
styles = ['darkgrid','dark','white','whitegrid','tricks'] # 颜色代表背景颜色，grid代表是否有网格
# style是seaborn本身定义好的
sns.set_style(style[0]) # 进行装饰
sinplot() # 经过修饰之后的图像

sns.axes_style() # 显示当前主题的内容，这些数据都可以修改微调
# 更改的时候就将其信息的字典复制到set_style()里，当做参数来修改，注意是以字典的形式
sns.set() # 设置风格为空，即清空自己定义的，恢复到默认的时候

2、plotting_context() and set_context()
context = ['paper','notebook','talk','poster'] # seaborn本身定义好的
sns.set_context('paper',rc={'grid.linewidth':3.0}) # rc参数
sinplot()

sns.plotting_context() # 显示出当前状态的数据
sns.set() # 恢复到默认


'''
强大的调色功能
'''
def sinplot1():
	x = np.linspace(0,14,100)
	plt.figure(figsize=(8,6)) # 图像比较小时，通过这个函数更改大小
	for i in range(4):
		plt.plot(x,np.sin(x+i)*(i+0.75),label='sin(x+%s)*(%s+0.75)' % (i,i))
	plt.legend()
sinplot1()

# 引入seaborn
sns.color_palette() # 使用调色板
# 不传入参数返回当前使用的调色板（RGB）
sns.palplot(sns.color_palette()) # 画出调色板，参数为上面的调色板
pal.style = ['deep','nuted','pastel','bright','dark','colorblind'] # seaborn默认定义的调色板
sns.set_palette(sns.color_palette('dark')) # 设置色板
sns.set() # 恢复默认风格

# 第二种设置画板方式，并且最后恢复到默认
with sns.color_palette():
	sinplot1() # 在内部调整画板输出图形，当with结束时，则恢复默认

# 默认提供的色板数量是固定的，如果图像是更多的函数，那么颜色将循环色板中的风格。如果想不使他颜色有相同，可以通过sns.color_palette（）来修改
sns.color_palette([(0.5,0.2,0.6),(0.3,0.3,0.4)]) # 因为色板是以列表的形式存储的，里面的每种风格以元组的形式存在所以需要用[()]

# 第二种增加色板颜色的方法
sns.color_palette('hls',8) # hls方法，后面写参数8，即生成有8种不同颜色的色板