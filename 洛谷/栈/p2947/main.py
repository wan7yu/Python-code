from collections import deque
stack = deque()
n = int(input())

ans = [0] * 100000
h = [0] * 100000

for i in range(1, n+1):
    h[i] = int(input())
# 反向遍历牛的身高
for j in range(n, 0, -1):
    while stack and h[stack[-1]] <= h[j]:
        stack.pop()
    if not stack:
        ans[j] = 0
    else:
        ans[j] = stack[-1]
    stack.append(j)
for k in range(1, n+1):
    print(ans[k])
