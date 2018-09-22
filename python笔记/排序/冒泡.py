def bubble_sort(array):
    # 外层循环确定一共需要循环几趟
    for i in range(len(array) - 1):
        # 内层循环，相邻的两个元素比较，大的向后移，直到把最大的移到最后，下一次继续，只需要比较到上一次确定大小之前
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

lis = [2, 3, 4, 3, 4, 223, 4, 56, 7, 1]
print(bubble_sort(lis))

# O(n**2) 稳定

# 改进，如果一趟之后，没有发生位置交换，则说明排序完成，结束
# def bubble_sort(array):
#     for i in range(len(array)-1):
#         current_status = False
#         for j in range(len(array) - i -1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 current_status = True
#         if not current_status:
#             break
