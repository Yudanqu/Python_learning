def select_sort(array):
	for i in range(len(array)-1):
		min = i
		# 选择出最小的元素的下标，之后进行交换
		for j in range(i+1,len(array)):
			if array[j] < array[min]:
				min = j
		array[i],array[min] = array[min],array[i]
	return array


lis = [2, 3, 4, 3, 4, 223, 4, 56, 7, 1]
print(select_sort(lis))