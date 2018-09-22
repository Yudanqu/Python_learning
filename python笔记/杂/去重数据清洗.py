# 通过去重进行数据清洗

df['columns'].duplicated() # 显示是否为唯一的，若前面出现过，则为True，若没有出现过，则为False
df['columns'].unique() # 显示不重复的数据，可以用来统计数量

df['columns'].drop_duplicated() # 删除里面为True的数据，即重复的数据，但这仅仅是对这个columns的去重
df.drop_duplicated(['columns']) # 此时则是根据这一列，对整个数据进行去重
# drop_duplicated里的参数：keep是指当有重复时保留哪一个，默认为first，还有last等等