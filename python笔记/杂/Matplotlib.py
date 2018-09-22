import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
plt.plot(x,y)

a = [1,2,3]
b = [4,5,6]
plt.plot(a,b,'*')

t = np.arange(0,10,0.1)
s = np.sin(t*np.pi)
plt.plot(t,s,'b*',label='aaa')
plt.plot(t*2,s,'r--',label='bbb')
plt.xlabel('this is x')
plt.ylabel('this is y')
plt.title('xxx')
plt.legend()
plt.show()

plt.subplot(2,1,1) # 子图 =plt.subplot(211)

a = plt.subplots()
# 返回两个对象 figure ax
figure,ax = plt.subplots()
ax.plot([1,2,3,4,5])
plt.show() # 显示图像

# subplots可以传入参数，几行几列，plt.subplots(2,2)
figure,ax = plt.subplots(2,2)
figure # 显示画布，分成2*2的
# 画图
ax[0][0].plot(x,y)
ax[0][1].plot(x*2,y*2)

# 对pandas中的Series进行绘图
import pandas as pd
from pandas import Series,DataFrame
plot参数：kind:图像显示的方法，包括'line''bar''barh''hist''box''kde''density''area''pie'.
		  grid=True 表示显示背景的网格
		  label='str',参数里写这个，输出图像之前要协一个plt.legend()，显示图例
		  title='str',显示标题
		  style='--',显示为虚线
plt.legend() # 显示图例

s1 = Series(np.random.randint(1000).cumsum()) # 创建series，cumsum()是指叠加求和，本位数是前几项之和
s1.plot() # series有自己的plot函数

# 对pandas中的DataFrame进行绘图
df = DataFrame(
	np.random.randint(1,10,40).reshape(10,4),
	columns=['A','B','C','D']
	)
df.plot() # dataframe也有自己的plot，按列画出来，参数包含ax，选择输出的画布
参数：stacked=True,表示一个堆叠的情况，同一个index下，columns一不同颜色叠在一起

1、可以取其一行或几行来画图，即将dataftame横过来画：
一行：df.iloc[5].plot()
多行或全部：for i in df.index:
				df.iloc[i].plot(label=str[i])
			plt.legend()
2、对列画图：
df['A'].plot()

3、对行画还有简便方法：
就是对df进行转置，然后再plot ，df.T.plot()



直方图和密度图：
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame

# 直方图
s = Series(np.random.randn(1000))
plt.hist(s,rwidth=0.9) # 直方图,rwidth为设置宽度
plt.show()
hist()的参数：rwidth为宽度；bins=20表示显示的区间，默认是10份；color='r'设置颜色；

# 密度图
s.plot(kind='kde') # kind='kde'即表示密度图