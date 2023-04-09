def add(digits, n):
    if digits[n] < 9 and n >= 0:
        digits[n] += 1
        print('123', digits)
        return digits
    elif digits[n] == 9 and n >= 0:
        digits[n] = 0
        n -= 1
        return add(digits, n)
    elif n == -1:
        digits[0] = 1
        digits.append(0)
        print('123', digits)
        return digits


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    n = len(digits)-1
    digits = add(digits, n)
    return digits


print(plusOne([9]))


# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         n = len(digits)
#         # 逆序找到第一个不为9的数
#         for i in range(n - 1, -1, -1):
#             if digits[i] != 9:
#                 digits[i] += 1
#                 # 让这个数后面的所有数变成0
#                 for j in range(i + 1, n):
#                     digits[j] = 0
#                 return digits

#         # digits 中所有的元素均为 9
#         return [1] + [0] * n
