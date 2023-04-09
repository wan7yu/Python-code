# # 借助gcd求lcm(最小公倍数)

# def gcd(a: int, b: int):
#     """辗转相除法"""
#     while True:
#         c = a % b
#         if c != 0:
#             a = b
#             b = c
#         else:
#             return b


# def lcm(a, b):
#     return a*b // gcd(a, b)


# print(lcm(7, 28))
AB = 52.1
BC = 57.2
CD = 43.5
DE = 51.9
EA = 33.4
EB = 68.2
EC = 71.9
s1 = (AB+EA+EB)/2
s2 = (EB+EC+BC)/2
s3 = (EC+DE+CD)/2

A1 = (s1*(s1-AB)*(s1-EA)*(s1-EB)) ** 0.5
A2 = (s2*(s2-EB)*(s2-EC)*(s2-BC)) ** 0.5
A3 = (s3*(s3-EC)*(s3-CD)*(s3-DE)) ** 0.5

num = A1+A2+A3
print(num)
