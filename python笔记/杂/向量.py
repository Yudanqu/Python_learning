import sys
from datetime import datetime
import numpy as np
#向量相加-python
def pythonsum(n):
	a = list(range(n))
	b = list(range(n))
	c = []
	for i in range(len(a)):
		a[i] = i ** 2
		b[i] = i ** 3
		c.append(a[i]+b[i])
	return c
start = datetime.now()
#print(pythonsum(5))
q = pythonsum(1000000)
print('lated=',datetime.now()-start)

#向量相加-numpy
def numpysum(n):
	a = np.arange(n) ** 2
	b = np.arange(n) ** 3
	c = a + b
	return c
start1 = datetime.now()
#print(numpysum(5))
w = numpysum(1000000)
print('lated=',datetime.now()-start1)