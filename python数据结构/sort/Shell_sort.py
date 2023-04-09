# 希尔排序
import random


def insert_sort(li, gap):
    for i in range(gap, len(li)):     # 存放无序数的下标
        tmp = li[i]    # 存放需要比较的值
        j = i-gap         # 一组有序数的第一个下标（按gap分组）
        while j >= 0 and tmp <= li[j]:  # 当下标大于0且后面的数小于等于前面的数时
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp


def shell_sort(li):
    d = len(li) // 2    # 求出对应的gap
    while d >= 1:       # 只要gap大于等于1就调用插入排序
        insert_sort(li, d)
        d //= 2


li = [i for i in range(1000)]
random.shuffle(li)
print("原列表:", li)
shell_sort(li)
print("最终列表:", li)
