"""
　小蓝有一个充电器，可以使用不同的电压和电流充电。
　　给定充电器工作的记录，请计算在这个记录期间总共通过充电传输了多少电能。
输入格式
　　输入第一行包含一个整数 n ， 表示记录的条数。
　　接下来 n 行，每行包含一个时刻 T 和两个非负整数 U, I，
    表示在时刻 T 充电电压变为 U（单位伏），电流变为 I（单位A）。
    最后一行满足 U 和 I 均为 0，在前面的行中也可能出现 U、I 为 0 的情况。
    其中时间表示为 HH:MM:SS 的格式，时分秒分别用两位十进制数表示（补前导零）。
　　输入保证时刻依次递增且在 00:00:00 至 23:59:59 的区间内，不用考虑跨过零点充电的情况。
输出格式
　　输出一个整数，表示总共通电的电能为多少焦耳，其中 1 焦耳等于 1 伏乘以1 安乘以 1 秒。
样例输入
3
12:00:00 12 1
12:01:02 5 2
12:01:10 0 0
样例输出
824
评测用例规模与约定
　　对于所有评测用例，1 <= n <= 100， 0 <= U, I <= 100。
"""
from datetime import date, datetime
n = int(input("n的值"))
times = []
U = []
I = []
s = 0
j = 0  # 计算焦耳的次数
for index in range(n):
    time = input('时间')
    u = int(input('电压'))
    i = int(input('电流'))
    times.append(time)
    U.append(u)
    I.append(i)
while True:
    times[j] = datetime.strptime(times[j], "%H:%M:%S")
    if 1 <= j <= 2:
        ses = ((times[j+1]-times[j]).seconds) * u[j]*i[j]
        s += ses
    j += 1
    if j == n//2:
        break
print(s)
