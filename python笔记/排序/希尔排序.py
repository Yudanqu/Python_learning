def shell_sort(array):
	gap = len(array) // 2
	while gap > 0:
		for i in range(gap,len(array)):
			tmp = array[i]
			j = i - gap
			while j > 0 and array[j] > array[i]:
				array[i] = array[j]
				j -= gap
			array[j+gap] = tmp
		gap //= 2


lis = [2, 3, 4, 3, 4, 223, 4, 56, 7, 1]
shell_sort(lis)
print(lis)

 # 时间复杂度:O((1+τ)n)