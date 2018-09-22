lis = [1,2,3,4,5]
def fn(x):
	return x**2
res = map(fn,lis)
print(res)
# print(list(res))
print([x for x in res if x>=10])
