"""
求m区间内的最小值
## 题目描述
一个含有 n 项的数列，求出每一项前的 m 个数到它这个区间内的最小值。

若前面的数不足 m 项则从第 1 个数开始，若前面没有数则输出 0。

## 输入格式

第一行两个整数，分别表示 n，m。

第二行，n 个正整数，为所给定的数列 ai。

## 输出格式

n 行，每行一个整数，第 i 个数为序列中 a_i 之前 m 个数的最小值。

样例输入
6 2
7 8 1 4 3 2
样例输出 
0
7
7
1
1
3
"""
from collections import deque

# 队列
q = deque()
# 具有n个元素的序列,维护区间的长度m
n, m = map(int, input().split())
# 序列元素
lis = [0] + list(map(int, input().split()))
print(0)
for i in range(1, n):
    while q and lis[q[-1]] > lis[i]:
        q.pop()
    q.append(i)
    if q[0] <= i-m:
        q.popleft()
    print(lis[q[0]])
