def insert_sort(array):
        # 从第二个元素开始插入，以第一个元素为基准做比较，比他小的往前放
    for i in range(1, len(array)):
        min = array[i]
        # 取到紧邻要插元素的前一个，比较大小，若比前一元素小，则把前一个元素复制到后面一份，直到找到合适的位置，把min插入
        j = i - 1
        # 找适当位置
        while j >= 0 and array[j] > min:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = min
    return array


lis = [2, 3, 4, 3, 4, 223, 4, 56, 7, 1]
print(insert_sort(lis))

# 排序部分为有序区，待插入部分为无序区
# O(n**2)  稳定
