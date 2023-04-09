"""
洛谷P1160
"""


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        self.flag = True


# n个同学
n = int(input())
# 创建一个n大小的列表
a = [None for i in range(n+1)]
# 定义前一个a[0]
# 此时k就代表下标
a[0] = Node(0, a[0], a[0])
a[1] = Node(1, a[0], a[0])
a[0].right = a[1]
a[0].left = a[1]
for i in range(2, n+1):
    k, p = map(int, input().split())
    # 插入到左边
    if not p:
        a[i] = Node(i, a[k].left, a[k])
        a[k].left.right = a[i]
        a[k].left = a[i]
    # 插入到右边
    else:
        a[i] = Node(i, a[k], a[k].right)
        a[k].right.left = a[i]
        a[k].right = a[i]
# 删除
m = int(input())
for i in range(m):
    x = int(input())
    # 直接标记，不删除结点
    a[x].flag = False

cur = a[0]
# 输出
while cur.right != a[0]:
    cur = cur.right
    if cur.flag:
        print(cur.val, end=" ")
