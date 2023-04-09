"""
表达式求值

## 题目描述

给定一个只包含加法和乘法的算术表达式，请你编程计算表达式的值。

## 输入格式
一行，为需要你计算的表达式，
表达式中只包含数字、加法运算符 + 和乘法运算符 *，
且没有括号，所有参与运算的数字均为 0 到 2^{31}-1 之间的整数。  

输入数据保证这一行只有 0-9、+、*  这 12种字符。

## 输出格式

一个整数，表示这个表达式的值。  

注意：当答案长度多于 4 位时，请只输出最后 4 位，前导 0 不输出。

样例1
样例输入
1+1*3+4
样例输出
8
样例2
样例输入
1+1234567890*1
样例输出 
7891
## 样例3
样例输入
1+1000000003*1
样例输出
4
"""
from collections import deque
# q存放计算的结果
q = deque()
# 定义全局变量
global need, num, top
need = False
# num存放数字，top代表栈顶元素
num, top = 0, 0


def handle():
    global num, need, top
    # 如果是*号
    if need:
        top = q[-1]
        q.pop()
        q.append(num*top % 10000)
    else:
        q.append(num % 10000)
    num = 0


def main():
    global num, need, top
    s = input()
    for i in range(len(s)):
        # 是*号则调用处理函数
        # 注意need 在下一次才能用到
        if s[i] == '*':
            handle()
            need = True
        # 是+号则先处理*号
        elif s[i] == '+':
            handle()
            need = False
        # 否则拼接起来
        else:
            num = int(s[i]) + num * 10
    # 如果还有没结束的*法操作就处理掉
    handle()
    # 对栈内结果相加
    while q:
        top = q[-1]
        q.pop()
        num = (top+num) % 10000
    print(num)
    return 0


main()
