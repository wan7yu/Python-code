# 最大公约数

# def gcd(a: int, b: int):
#     """辗转相除法"""
#     while True:
#         c = a % b
#         if c != 0:
#             a = b
#             b = c
#         else:
#             return b

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(14, 28))
