# 基数排序
import random


def radix_sort(li):
    # 取最大的数，即为最大位数
    max_num = max(li)
    it = 0
    # 只要对应的位数小于最大位数
    while 10 ** it <= max_num:
        backets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            backets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in backets:
            li.extend(buc)
        # 写回列表
        it += 1


li = [i for i in range(100000)]
random.shuffle(li)
radix_sort(li)
print(li)
