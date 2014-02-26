target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [0 for x in range(target+1)]
ways[0] = 1
for coin in coins:
    print (coin)
    for i in range(coin,target+1):
        print(ways[i - coin], i , coin)
        ways[i] += ways[i - coin]
print(ways)
