# 数据聚合技术Aggregation
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = DataFrame()
df['city'] = ['A','A','A','A','B','B','B','B','C','C']
df['count'] = np.random.randint(20,80,size=len(df['city']))
g = df.groupby(df['city'])

g.agg('min') # 找最小值
def foo(attr):
	return attr.max() - attr.min()
g.agg(foo) # 通过自定义的函数聚合

g.get_group('A') # 多个columns时要用元组方式传入