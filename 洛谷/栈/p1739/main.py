"""
1739 表达式括号匹配
"""
"""
需要注意的点:
右括号不能比左括号先出现
"""
s = input()
zuo, you = 0, 0
for i in s:
    if i == '@':
        break
    if i == '(':
        zuo += 1
    elif i == ')':
        you += 1
    if you > zuo:
        break
if zuo == you:
    print('YES')
else:
    print('NO')
