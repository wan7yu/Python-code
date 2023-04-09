"""
中缀表达式转后缀表达式
"""
from collections import deque
# 数字栈
num = deque()
# 符号栈
opt = deque()
# 另外的栈
dat2 = deque()
dat = deque()


def check(t):
    # 优先级
    if t == '+' or t == '-':
        return 1
    elif t == '*' or t == '/':
        return 2
    elif t == '^':
        return 3
    elif t == '(' or t == ')':
        return 0
    else:
        return -1


def transfer(s):
    for i in s:
        if '0' <= i <= '9':
            dat.append(i)
        elif i == '(':
            opt.append(i)
        elif i == ')':
            t = opt[-1]
            while t != '(':
                opt.pop()
                dat.append(t)
                t = opt[-1]
            else:
                opt.pop()
        # 是运算符
        elif check(i) >= 1 and check(i) <= 3:
            if opt:
                t = opt[-1]
                while opt and check(i) <= check(t):
                    if check(i) == check(t) and i == '^':
                        break
                    opt.pop()
                    dat.append(t)
                    if opt:
                        t = opt[-1]
            opt.append(i)
    while opt:
        t = opt[-1]
        opt.pop()
        dat.append(t)
    while dat:
        t = dat[-1]
        dat.pop()
        opt.append(t)
    while opt:
        t = opt[-1]
        print(t, end=' ')
        opt.pop()
        dat.append(t)
    print()


def js(p1, p2, t):
    if t == '+':
        return p1+p2
    elif t == '-':
        return p1-p2
    elif t == '*':
        return p1*p2
    elif t == '/':
        return p1//p2
    else:
        return p1**p2


def cal():
    while dat:
        t = dat[-1]
        dat.pop()
        opt.append(t)
    while opt:
        t = opt[-1]
        opt.pop()
        if '0' <= t <= '9':
            num.append(int(t))
        else:
            p2 = num[-1]
            num.pop()
            p1 = num[-1]
            num.pop()
            num.append(js(p1, p2, t))
            while num:
                t = num[-1]
                num.pop()
                dat2.append(t)
            while dat2:
                t = dat2[-1]
                print(t, end=' ')
                dat2.pop()
                num.append(t)
            while opt:
                t = opt[-1]
                print(t, end=' ')
                opt.pop()
                dat.append(t)
            while dat:
                t = dat[-1]
                dat.pop()
                opt.append(t)
            print()


# 表达式
s = input()
# 后缀表达式
transfer(s)
cal()
