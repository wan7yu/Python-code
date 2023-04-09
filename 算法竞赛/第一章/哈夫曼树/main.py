"""
利用贪心思想
带权路径最短的最优树
poj 1521
"""
from queue import PriorityQueue
q = PriorityQueue()


def solution(s):
    sorted(s)
    num = 1
    for i in range(0, len(s)):
        if i < len(s)-1:
            if s[i] != s[i+1]:
                q.put(num)
                num = 1
            else:
                if i == len(s)-2:
                    num += 1
                    break
                num += 1
        else:
            q.put(num)

    ans = 0
    # 当只有一个字符时
    if q.qsize() == 1:
        ans = len(s)
    while q.qsize() > 1:
        # 获取每个字符出现次数
        a = q.get()
        b = q.get()
        q.put(a+b)
        ans = ans + a+b
    q.get()
    print('%d %d %.1f' % (len(s)*8, ans, float(len(s)*8/ans)))


lis = []
while True:
    s = input()
    if s == 'END':
        break
    else:
        lis.append(s)
for i in lis:
    solution(i)
