import random
"""
堆排序(首先满足:这个堆是完全二叉树)
思路:1.先建堆。2.向下调整成大根堆。
    3.出数。4.向下调整保持大根堆
    5.重复3、4.
**堆的向下调整性质
    sift函数：
如果父亲节点比孩子节点小，就将孩子节点中最大的数放到父亲节点位置
再继续向下重复上面步骤。直到所有父亲节点比孩子节点大
**建堆:
从最后一个元素的父亲节点开始，调用sift函数，调整成大根堆
依次向上直到建堆完成。
**出数:
从最后一个元素开始，与根节点交换
调用sift函数，调整剩余的元素为大根堆。
"""


def sift(li, low, high):       # 向下调整函数
    i = low         # i最开始指向根节点
    j = 2 * i + 1   # j开始是左孩子
    tmp = li[low]   # 把堆顶元素存放起来
    while j <= high:        # 只要j位置有数
        if j+1 <= high and li[j+1] > li[j]:     # 如果有右孩子并且比左孩子大
            j = j+1         # 让j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j           # 往下一层
            j = 2*i+1
        else:           # tmp大，则把tmp放在i的位置
            # li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        # i表示建堆的时候调整的部分的根的下标
        sift(li, i, n-1)
    # 建堆完成了
    for i in range(n-1, -1, -1):    # 出数，调用向下调整函数
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)  # i-1是新的high


li = [i for i in range(20)]
random.shuffle(li)
print("The original list:", li)

heap_sort(li)
print("The final list:", li)
