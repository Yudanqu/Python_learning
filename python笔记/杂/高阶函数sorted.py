排序：
sorted(iterable)

普通排序：
lis1 = [3,4,5,3,5,7,8,6,9]
lis2 = sorted(lis1)
print(lis1)
print(lis2)

绝对值排序：
lis3 = [3,4,-5,3,5,-7,8,6,9]
# key接受函数来实现自定义排序规则，可以是系统的也可以是自定义的
lis4 = sorted(lis3, key = abs)
print(lis3)
print(lis4)

降序排序：
reverse=True