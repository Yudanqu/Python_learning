#通过apply方法进行数据的预处理

#通过apply修改其中一个columns的大小写（通过函数）
df1 = pd.read_csv('F:\\python\\table.csv')
s1 = Series(['a']*2346)
df1['工作2'] = s1
df1['工作2'] = df1['工作2'].apply(str.upper)
# 如果需要进行其他操作，可以写函数，作为apply的参数进行数据处理