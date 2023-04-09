# 冒泡排序

import random


def buddle_sort(li):
    for i in range(len(li)-1):  # 第i趟
        mark = False            # 定义标志，如果没有交换则说明排序完成，退出
        for j in range(len(li)-i-1):    # 初始指针位置
            if li[j] > li[j+1]:         # 如果前面的数比后面的大交换它们
                li[j], li[j+1] = li[j+1], li[j]
                mark = True
        if not mark:
            return
        print("第%d趟:" % (i), li)


li = list(random.randint(0, 100) for i in range(10))
print("初始列表:", li, "\n")
buddle_sort(li)
print()
print("最终列表:", li)
