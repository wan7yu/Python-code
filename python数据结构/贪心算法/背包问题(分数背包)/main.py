"""
分数背包
一个正在抢劫商店的小偷发现了n个商品，第i个商品价值vi美元，重wi磅，vi和wi都是整数。
这个小偷希望拿走价值尽量高的商品，但他的背包最多能容纳W磅重的商品，W是一个整数
他应该拿那些商品呢？
分数背包(对于每个商品，小偷可以拿走一部分，而不是只能全部拿走或者不拿走)
"""
# (价格，重量)
goods = [(60, 10), (120, 30), (100, 20)]
goods.sort(key=lambda x: x[0]/x[1], reverse=True)


def fractional_backpack(goods, w):
    num = [0] * len(goods)
    val = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            num[i] = 1
            val += price
            w -= weight
        else:
            num[i] = w/weight
            val += num[i] * price
            w = 0
            break
    return val, num


print(fractional_backpack(goods, 50))
