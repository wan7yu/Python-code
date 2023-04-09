# 计数排序
import random


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        # print(val)
        for i in range(val):
            li.append(ind)
            # print(ind)


li = [random.randint(0, 100) for i in range(1000)]
# print(li)
count_sort(li)
print(li)
