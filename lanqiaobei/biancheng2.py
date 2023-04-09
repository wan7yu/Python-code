"""
输入一个由小写英文字母组成的字符串，请将其中的元音字母（a, e, i, o, u)转换成大写，其它字母仍然保持小写。
输入格式
　　输入一行包含一个字符串。
输出格式
　　输出转换后的字符串。
样例输入
lanqiao
样例输出
lAnqIAO
评测用例规模与约定
　　对于所有评测用例，字符串的长度不超过100。
"""
s = input()
obj = list(s)

if len(s) <= 100:
    for i in range(len(s)):
        if obj[i] in ['a', 'e', 'i', 'o', 'u']:
            obj[i] = obj[i].upper()
    s = ''.join(obj)

print(s)
