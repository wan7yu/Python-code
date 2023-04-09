"""
静态链表
p1996
"""
N = 105


class Node:
    def __init__(self, id=None) -> None:
        self.id = id
        self.nextid = None


class StLinkList:
    def __init__(self) -> None:
        self.head = None
        self.lis = [Node() for i in range(N)]


tmp = input('').split()
n, m = int(tmp[0]), int(tmp[1])
li = StLinkList().lis
li[0].nextid = 1
for i in range(1, n+1):
    li[i].id = i
    li[i].nextid = i+1
li[n].nextid = 1
now, pre = 1, 1
while n > 1:
    for i in range(1, m):
        pre = now
        now = li[now].nextid
    print(li[now].id, end=' ')
    li[pre].nextid = li[now].nextid
    now = li[pre].nextid
    n -= 1
print(li[now].nextid, end=" ")
