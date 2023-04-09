"""
给定一些数字，将他们拼接成最大的数
32、94、128、1286、6、71
94-71-6-32-1286-128
"""
li = [32, 94, 128, 1286, 6, 71]


def b_sort(li):
    for i in range(len(li)):
        for j in range(len(li)-1):
            if li[j] + li[j+1] < li[j+1] + li[j]:
                li[j], li[j+1] = li[j+1], li[j]
            else:
                continue


def number_join(li):
    li = list(map(str, li))
    b_sort(li)
    return "".join(li)


print(number_join(li))
