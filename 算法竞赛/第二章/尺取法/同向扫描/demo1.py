"""
寻找区间和

给定一个长度为 n 的数组 a[] 和一个数 S 
在这个数组中找到一个区间，使这个区间的数组元素之和等于S。
输出区间的起点和终点位置。
输入样例：
15
6 1 2 3 4 6 4 2 8 9 10 11 12 13 14
6

输出样例：
0 0
1 3
5 5
6 7
"""


def findsum(a, n, s):
    i, j = 0, 0
    nsum = a[0]
    while j < n:
        if nsum >= s:
            if nsum == s:
                print(i, j)
            nsum -= a[i]
            i += 1
            if i > j:
                nsum = a[i]
                j += 1
        else:
            j += 1
            nsum += a[j]


a = [6, 1, 2, 3, 4, 6, 4, 2, 8, 9, 10, 11, 12, 13, 14]
n = 15
s = 6
findsum(a, n-1, s)
