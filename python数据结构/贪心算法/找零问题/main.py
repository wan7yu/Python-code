"""
假设商店老板需要找零n元钱,
钱币的面额有:100元、50元、20元、5元、1元,
如何找零使得所需钱币的数量最少?
"""
currency1 = [100, 1, 50, 20, 5]
currency2 = [100, 50, 20, 5]

currency1.sort(reverse=True)


def change(currency, n):
    m = [0] * len(currency)
    for i, money in enumerate(currency):
        m[i] = n // money
        n = n % money
    return m, n


print(change(currency1, 352))
