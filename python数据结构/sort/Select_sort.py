def select_sort(li):
    for i in range(len(li)-1):      # 循环n-1次，最后一个一定为有序数
        min_loc = i
        for j in range(i+1, len(li)):   # j从第二个值开始，不用与自己比较
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:                # 有比i对应的值小的且不是本身就交换
            print(li)
            li[i], li[min_loc] = li[min_loc], li[i]


li = [1, 4, 2, 3, 5, 6, 7, 8, 9]
select_sort(li)
print(li)
