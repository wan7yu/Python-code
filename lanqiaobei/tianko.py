word = list(input())       # 将输入的字符串转换成列表
word.sort()     # 对列表排序，解决出现次数相同的字符时的字典序问题
a = 0       # 默认次数
li = []     # 存放新列表
print(word)
for i in word:      # 找出字符出现最大的次数
    n = word.count(i)
    if n > a:
        a = n

for j in word:      # 找出对应次数的字符，添加到列表中
    if word.count(j) == a:
        li.append(j)

print(li[0])
print(a)
