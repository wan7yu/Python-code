def insert_sort(li):
    for i in range(1, len(li)):     # 存放无序数的下标（第二个数——最后一个数）
        tmp = li[i]     # 存放需要比较的值
        j = i-1         # 第一个有序数的下标（第一个数）
        while j >= 0 and tmp <= li[j]:  # 当下标大于0且后面的数小于等于前面的数时
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)


li = [3, 2, 4, 1, 5, 7, 9, 6, 8]
print(li)
insert_sort(li)
