"""
双端队列（deque，全名double-ended queue），是一种具有队列和栈的性质的数据结构。
双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。
双端队列可以在队列任意一端入队和出队。
"""
# add_front(item) 从队头加入一个元素
# add_rear(item) 从队尾加入一个元素
# remove_front() 从队头删除一个元素
# remove_rear() 从队尾删除一个元素
# is_empty() 判断双端队列是否为空
# size() 返回队列的大小


class dequeue:
    def __init__(self) -> None:
        self.val = [0]
        self.rear = 0
        self.head = 0

    def is_empty(self) -> bool:
        return len(self.val) == 0

    def size(self):
        return len(self.val)

    def add_front(self, val):
        self.val.insert(0, val)

    def add_rear(self, val):
        self.val.append(val)

    def remove_front(self):
        val = self.val.pop(0)
        return val

    def remove_rear(self):
        val = self.val.pop()
        return val
