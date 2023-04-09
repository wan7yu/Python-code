"""
洛谷p5788
"""
# python会爆内存
from collections import deque
M_SIZE = 10000000

s = deque()
n = int(input())
lis = list(map(int, input().split()))
a = [0]*M_SIZE
f = [0]*M_SIZE
for i in range(n):
    a[i+1] = lis[i]
for i in range(n, 0, -1):
    while s and a[s[-1]] <= a[i]:
        s.pop()
    if not s:
        f[i] = 0
    else:
        f[i] = s[-1]
    s.append(i)
for i in range(1, n+1):
    print(f[i], end=' ')
