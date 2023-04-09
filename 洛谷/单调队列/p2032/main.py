"""
# 扫描

## 题目描述

有一个 1 * n 的矩阵，有 n 个整数。

现在给你一个可以盖住连续 k 个数的木板。

一开始木板盖住了矩阵的第 1 ~ k 个数，
每次将木板向右移动一个单位，直到右端与第 n 个数重合。

每次移动前输出被覆盖住的数字中最大的数是多少。

## 输入格式

第一行两个整数 n,k，表示共有 n 个数，木板可以盖住 k 个数。

第二行 n 个整数，表示矩阵中的元素。

## 输出格式

共 n - k + 1 行，每行一个整数。

第 i 行表示第 i ~ i + k - 1 个数中最大值是多少。

### 样例输入 
5 3
1 5 3 4 2
### 样例输出 
5
5
4
"""
from collections import deque

q = deque()
# n：n个数 k：盖住的范围
n, k = map(int, input().split())
lis = [0] + list(map(int, input().split()))
for i in range(1, n+1):
    while q and lis[q[-1]] < lis[i]:
        q.pop()
    q.append(i)
    if q and q[0] <= i-k:
        q.popleft()
    if i >= k:
        print(lis[q[0]])
