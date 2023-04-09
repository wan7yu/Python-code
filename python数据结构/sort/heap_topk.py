"""
topk问题:
给定n个数，求前k个最大数（k<n)
"""
import random


def sift(li, low, high):       # 向下调整函数
    i = low         # i最开始指向根节点
    j = 2 * i + 1   # j开始是左孩子
    tmp = li[low]   # 把堆顶元素存放起来
    while j <= high:        # 只要j位置有数
        if j+1 <= high and li[j+1] < li[j]:     # 如果有右孩子并且比左孩子大
            j = j+1         # 让j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j           # 往下一层
            j = 2*i+1
        else:           # tmp大，则把tmp放在i的位置
            li[i] = tmp
            break
    else:
        li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    # 1.建堆
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 2.遍历
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    # 3. 出数
    return heap


li = list(range(1000))
random.shuffle(li)

print(topk(li, 10))
