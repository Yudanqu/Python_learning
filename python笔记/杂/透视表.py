# 透视表
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = pd.read_excel('F:/建模竞赛_校赛/附件一.xlsx')
pd.pivot_table(df, index=['工作2']) # 去掉重复的
# 里面参数aggfunc='mean'默认聚合方法为mean。可以修改，例如aggfunc='sum'。
# index可以输入多个，eg：index=['A','B']
# 显示数据也可以指定，有个参数是values，默认等于none，通过列表传入