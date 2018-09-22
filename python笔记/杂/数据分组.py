# 数据分组技术GroupBy
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = DataFrame()
df['city'] = ['A','A','A','A','B','B','B','B','C','C']
df['count'] = np.random.randint(20,80,size=len(df['city']))
g = df.groupby(df['city'])

g.groups # 返回分组
df_1 = g.get_group('A')
# 之后可以对df_1做操作，例如求平均数之类的
# 也可以对g直接做操作，例如g.mean()即对每组求平均
