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


a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print("This value's index is %s" % (binary_search(a, 13)))
print("This value's index is %s" % (binary_search(a, 6)))
