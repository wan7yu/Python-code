"""
后缀表达式
"""
from collections import deque

q = deque()


def opt(op):
    ans = 0
    if len(q) >= 2:
        p2 = q.pop()
        p1 = q.pop()
        if op == '+':
            ans = p2+p1
        elif op == '*':
            ans = p2*p1
        elif op == '-':
            ans = p1-p2
        else:
            ans = p1//p2
        return ans
    else:
        return


def main():
    # 表达式
    s = input()
    num = 0
    for i in s:
        if '0' <= i <= '9':
            num = int(i) + num * 10
        elif i == '.':
            q.append(num)
            num = 0
        elif i == '@':
            break
        else:
            num = opt(i)
            q.append(num)
            num = 0
    return q.pop()


print(main())
