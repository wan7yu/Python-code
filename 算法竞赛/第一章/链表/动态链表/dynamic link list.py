"""
动态链表
约瑟夫问题（洛谷P1996）
"""
# 单向循环链表


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class DyLinkList:
    def __init__(self) -> None:
        self.head = None


tmp = input('').split()
n, m = int(tmp[0]), int(tmp[1])
head = DyLinkList().head
for i in range(1, n+1):
    if not head:
        head = Node(i)
        pre = head
        continue
    elif not pre.next:
        pre.next = Node(i)
        pre = pre.next
        continue
pre.next = head
now = head
p = head
while n > 1:
    for i in range(1, m):
        p = now
        now = now.next
    print(now.val, end=' ')
    p.next = now.next
    del now
    now = p.next
    n -= 1
print(now.val)
del now
