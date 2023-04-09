coins = [1, 2, 5]
money = int(input())
cur = [0]*len(coins)
for i in range(len(coins)-1, -1, -1):
    cur[i] = money//coins[i]
    money = money-cur[i]*coins[i]
for i in range(len(cur)):
    print(coins[i], ':', cur[i])
