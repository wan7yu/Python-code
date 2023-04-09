class dequeue:
    def __init__(self) -> None:
        # 存放的是索引
        self.val = []

    def is_empty(self) -> bool:
        return len(self.val) == 0

    def push_front(self, val):
        # 入队头
        self.val.insert(0, val)

    def push_back(self, val):
        # 入队尾
        self.val.append(val)

    def front(self):
        # 返回队头的编号
        if not self.is_empty():
            return self.val[0]

    def back(self):
        # 返回队尾的编号
        if not self.is_empty():
            return self.val[-1]

    def pop_front(self):
        # 删除队头，不返回值
        if not self.is_empty():
            self.val.pop(0)

    def pop_back(self):
        # 删除队尾，不返回值
        if not self.is_empty():
            self.val.pop()


# 单调递减队列
# 队列大小
q = dequeue()
# 具有n个元素的序列,维护区间的长度k
tmp1 = input().split()
n, k = int(tmp1[0]), int(tmp1[1])
# 序列元素
lis = [0]
tmp2 = input().split()
for i in tmp2:
    lis.append(int(i))
# 求最小值
for i in range(1, n+1):
    while not q.is_empty() and lis[q.back()] > lis[i]:
        q.pop_back()
    q.push_back(i)
    if i >= k:
        while not q.is_empty() and q.front() <= i-k:
            q.pop_front()
        print(lis[q.front()], end=' ')

while not q.is_empty():
    q.pop_back()

print()

# 求最大值
for i in range(1, n+1):
    while not q.is_empty() and lis[q.back()] < lis[i]:
        q.pop_back()
    q.push_back(i)
    if i >= k:
        while not q.is_empty() and q.front() <= i-k:
            q.pop_front()
        print(lis[q.front()], end=' ')
