import random
from cal_time import *
import copy


@cal_time
def buddle_sort(li):
    for i in range(len(li)-1):  # 第i趟
        mark = False            # 定义标志，如果没有交换则说明排序完成，退出
        for j in range(len(li)-i-1):    # 初始指针位置
            if li[j] > li[j+1]:         # 如果前面的数比后面的大交换它们
                li[j], li[j+1] = li[j+1], li[j]
                mark = True
        if not mark:
            return
        # print("第%d趟:" % (i), li)


def partition(li, left, right):
    tmp = li[left]          # 随机存放第一个要归位的值
    while left < right:
        while left < right and li[right] >= tmp:    # left < right 至少要两个数比较
            right -= 1
        li[left] = li[right]         # 如果right对应的值小于tmp 将它放到前面
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]      # 如果left对应的值大于tmp 将它放到后面
        # print(li)
    li[left] = tmp           # 当左右指针指向相同的位置的时候 归位完成
    return left


def _quick_sort(li, left, right):
    if left < right:       # 至少要两个数才比较
        mid = partition(li, left, right)
        _quick_sort(li, left, mid-1)     # 递归排序一边
        _quick_sort(li, mid+1, right)


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)


li = list(range(10000))
random.shuffle(li)

li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)

quick_sort(li1)
buddle_sort(li2)

# print(li1)
# print(li2)
