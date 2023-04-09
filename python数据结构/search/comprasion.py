from cal_time import *


@cal_time
def liner_search(data_set, value):
    for i in range(0, len(data_set)):
        if data_set[i] == value:
            return i
    else:
        return None


@cal_time
def binary_search(li, val):  # 前提：找查的数组或者列表是有序的
    left = 0
    right = len(li) - 1
    while left <= right:    # 候选区有值
        mid = (left+right)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid左侧
            right = mid-1
        else:               # 待查找的值在mid右侧
            left = mid+1
    else:
        return None


a = list(range(1000000))
print(liner_search(a, 389900))
print(binary_search(a, 389900))
# vscode 不支持小于0.0的时间显示（且不支持科学计数法）
