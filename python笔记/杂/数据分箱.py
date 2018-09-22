# 数据分箱技术Binning
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

score_list = np.random.randint(25,100,size=20)
bins = [0,59,70,80,100]
score_cat = pd.cut(score_list,bins)
pd.value_counts(score_cat)

df = DataFrame()
df['score']=score_list
df['name']=[pd.util.testing.rands(3) for i in range(20)] # 生成随机字符串
df['Categories'] = pd.cut(score_list,bins,labels=['D','C','B','A']) # labels是对应于bins间隔设置的标签