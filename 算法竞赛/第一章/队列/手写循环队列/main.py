"""
循环队列
1.初始化方法 2.求队列长度 3.判断是否为空
4.删除队头元素 5.插入队尾元素 6.返回队首元素
"""


class queue:
    def __init__(self, maxsize=1000) -> None:
        self.head = 0
        self.rear = 0
        self.queue = [0] * maxsize
        self.size = maxsize

    def length(self):
        return (self.rear - self.head + self.size) % self.size

    def empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    def pop(self):
        if self.head == self.rear:
            raise ValueError("pop failed,the queue is empty!")
        else:
            e = self.queue[self.head]
            self.head = (self.head+1) % self.size
            return True

    def front(self):
        return self.queue[self.head]

    def push(self, val):
        if (self.rear + 1) % self.size == self.head:
            raise ValueError("push failed,the queue is full!")
        else:
            self.queue[self.rear] = val
            self.rear = (self.rear + 1) % self.size
            return True
