# 内置优先队列
from queue import PriorityQueue

q = PriorityQueue()
q.put(3)
q.put(2)
q.put(50)
q.put(32)

while not q.empty():
    print(q.get(), end='\n')
