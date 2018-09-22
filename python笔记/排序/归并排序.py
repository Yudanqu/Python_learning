def merge(array,low,mid,high):
	tmp = []
	i = low
	j = mid + 1
	while i <= mid and j <= high:
		if array[i] <= array[j]:
			tmp.append(array[i])
			i += 1
		else:
			tmp.append(array[j])
			j += 1
	while i <= mid:
		tmp.append(array[i])
		i += 1
	while j <= high:
		tmp.append(array[j])
		j += 1
	array[low:high+1] = tmp

def merge_sort(array,low,high):
	if low < high:
		mid = (low + high)//2
		merge_sort(array, low, mid)
		merge_sort(array, mid+1, high)
		merge(array, low, mid, high)

# 将列表分为两段，把小的放进tmp，递归，直到递归到仅两个数，出来的就是排好序的，然后在放在大列表里排序

lis = [2, 3, 4, 3, 4, 223, 4, 56, 7, 1]
merge_sort(lis, 0, len(lis)-1)
print(lis)

# 时间复杂度：O(nlogn)
# 稳定性:稳定



# 快排、堆排和归并的小结

# 三种排序算法的时间复杂度都是O(nlogn)

# 一般情况下，就运行时间而言：
# 　　　　快速排序 < 归并排序 < 堆排序

# 三种排序算法的缺点：
# 　　快速排序：极端情况下排序效率低
# 　　归并排序：需要额外的内存开销
# 　　堆排序：在快的排序算法中相对较慢