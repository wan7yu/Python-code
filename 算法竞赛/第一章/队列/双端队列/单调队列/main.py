"""
单调队列，顾名思义，是一种具有单调性的队列。众所周知，
单调性有单调递增和单调递减两种，相应的单调队列也分为单调递增队列和单调递减队列两种。

单调递增队列：保证队列头元素一定是当前队列的最小值，用于维护区间的最小值。
单调递减队列：保证队列头元素一定是当前队列的最大值，用于维护区间的最大值。

去尾操作 ：队尾元素出队列。当队列有新元素待入队，需要从队尾开始，删除影响队列单调性的元素，维护队列的单调性。
(删除一个队尾元素后，就重新判断新的队尾元素)
去尾操作结束后，将该新元素入队列。

删头操作 ：队头元素出队列。判断队头元素是否在待求解的区间之内，如果不在，就将其删除。
（这个很好理解呀，因为单调队列的队头元素就是待求解区间的极值）
取解操作 ：经过上面两个操作，取出 队列的头元素 ，就是 当前区间的极值 。
"""


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
n, k = map(int, input().split())
# 序列元素
lis = [0] + list(map(int, input().split()))
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
    while not q.is_empty() and lis[q.back()] < lis[i]:  # 删尾
        q.pop_back()
    q.push_back(i)
    if i >= k:
        while not q.is_empty() and q.front() <= i-k:    # 去头
            q.pop_front()
        print(lis[q.front()], end=' ')
