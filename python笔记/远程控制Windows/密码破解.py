# 排列：有序

import itertools

mylist = list(itertools.permutations([1,2,3,4], 3))
print(mylist)
print(len(mylist))

# n个元素中选m个：一个有 n! / (n-m)! 中情况


# 组合:没有顺序

import itertools

mylist = list(itertools.combinations([1,2,3,4], 3))
print(mylist)
print(len(mylist))

# n个元素中选m个：一个有 n! / m!(n-m)! 中情况


# 排列组合：

import itertools

mylist = list(itertools.product([1,2,3,4], repeat=3))
print(mylist)
print(len(mylist))




# 伤敌一千自损一万的破解密码
import time
import itertools

# mylist = list(itertools.product([1,2,3,4], repeat=3))
passwd = ("".join(x) for x in itertools.product("1234567890", repeat=3))

while True:
	try:
		time.sleep(1)
		strs = next(passwd)
		print(strs)
	except StopIteration as e:
		break