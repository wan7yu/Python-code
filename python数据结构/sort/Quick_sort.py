"""
快速排序
思路:1.双指针比较 2.递归
传入一个可迭代对象，取可迭代对象中任一元素，然后将其分为两部分
(元素可以相互比较)
通过递归调用划分函数使得：
    左边所有的的数都<=这个数
    右边所有的数都>=这个数
然后把这个数放回到中间位置
"""


def partition(li, left, right):
    tmp = li[left]          # 随机存放第一个要归位的值
    while left < right:
        while left < right and li[right] >= tmp:    # left < right 至少要两个数比较
            right -= 1
        li[left] = li[right]         # 如果right对应的值小于tmp 将它放到前面
        print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]      # 如果left对应的值大于tmp 将它放到后面
        print(li, 'left')
    li[left] = tmp           # 当左右指针指向相同的位置的时候 归位完成
    return left


def quick_sort(li, left, right):
    if left < right:    # 至少两个数才比较
        mid = partition(li, left, right)
        # 递归排序左、右
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


li = [5, 3, 6, 4, 8, 7, 1, 9, 2]
print("The original list is :", li)
quick_sort(li, left=0, right=len(li) - 1)
print("The ultimate list is :", li)
