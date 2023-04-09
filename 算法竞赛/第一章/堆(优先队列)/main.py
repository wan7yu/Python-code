"""
洛谷p3378
"""
# 洛谷oj超时
from queue import PriorityQueue

q = PriorityQueue()
n = int(input())
lis = []
for i in range(n):
    lis.append(list(map(int, input().split())))
for i in range(n):
    if lis[i][0] == 1:
        q.put(lis[i][1])
    elif lis[i][0] == 2:
        tmp = q.get()
        print(tmp)
        q.put(tmp)
    else:
        q.get()
