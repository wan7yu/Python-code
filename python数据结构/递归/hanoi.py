def hanoi(n, a, b, c):
    # 定义汉诺塔函数
    global count
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving  form %s to %s" % (a, c))
        count += 1
        hanoi(n-1, b, a, c)


count = 0   # 计算执行次数count = 2^n - 1
hanoi(3, "A", "B", "C")
print(count)
