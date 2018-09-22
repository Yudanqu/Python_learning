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

def quick_sort(array,left,right):
	if left < right:
		mid = partition(array, left, right)
		quick_sort(array, left, mid-1)
		quick_sort(array, mid+1, right)
		return array

lis = [2, 3, 4, 5, 33, 4, 58776, 423, 454, 444, 444, 1]
quick_sort(lis,0,len(lis)-1)
print(lis)