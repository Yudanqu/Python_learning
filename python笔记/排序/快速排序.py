def quick_sort(array,left,right):
	if left < right:
		# 把基准两边排列好之后，在继续分别排着两半，依次递归下去
		mid = partition(array, left, right)
		quick_sort(array, left, mid-1)
		quick_sort(array, mid+1, right)
		return array

# 取一个元素，作为基准，从两头开始比较，比他小的放左边，大的放右边
def partition(array,left,right):
	tmp = array[left]
	while left < right:
		while left < right and array[right] >= tmp:
			right -= 1
		array[left] = array[right]
		while left < right and array[left] <= tmp:
			left += 1
		array[right] = array[left]
	array[left] = tmp
	return left


lis = [2, 3, 4, 3, 4, 223, 4, 56, 7, 1]
print(quick_sort(lis, 0, len(lis)-1))


# 时间复杂度：O(nlogn)，一般情况是O(nlogn)，最坏情况（逆序）：O（n^2）
# 不稳定  快