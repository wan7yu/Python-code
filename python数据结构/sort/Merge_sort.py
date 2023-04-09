import random
"""
归并排序
思路:1.拆分 2.归并
**拆分：
将列表拆分为两个小列表，再递归调用本身
最终拆成n个只有单独一个数的列表(此时都是有序的)
**归并
将所有的小列表合并成一个大列表(在合并过程中排序)
"""


def merge(li, left, mid, right):      # 合并
    i = left                 # i指向最开始的元素
    j = mid+1               # j指向中间
    ltmp = []               # 定义临时空列表存放有序数
    while i <= mid and j <= right:       # 左右部分分别都有数
        if li[i] < li[j]:           # 如果左边的数小于右边
            ltmp.append(li[i])      # 添加到临时列表中
            i += 1
        else:
            ltmp.append(li[j])      # 右边小于左边
            j += 1                  # 添加到列表中
    while i <= mid:             # 右边已经没有数了
        ltmp.append(li[i])      # 将左边所有数添加到列表中
        i += 1
    while j <= right:            # 左边无数
        ltmp.append(li[j])      # 添加到列表中
        j += 1
    li[left:right+1] = ltmp       # 切片往回写


def merge_sort(li, left, right):      # 归并排序
    if left < right:
        mid = (left + right)//2
        merge_sort(li, left, mid)    # 递归调用将左列表分解
        merge_sort(li, mid+1, right)  # 将右列表分解
        merge(li, left, mid, right)   # 调用合并函数


li = [i for i in range(20)]
random.shuffle(li)
print("The original list is:", li)
merge_sort(li, 0, len(li)-1)
print("The final    list is:", li)
