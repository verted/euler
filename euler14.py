import time
start = time.time()
largestChainNum = 0
largestStartNum = 0
max = 1000000
cache = {}
for i in range(1, 10000):
    temp = i
    chainNum = 0
    while temp != 1:
        if temp >= i:
            if temp % 2 == 0:
                temp = temp/2
            else:
                temp = 3*temp+1
            chainNum +=1
        else:
            chainNum += cache[temp]
            break
    cache[i] = chainNum
    if chainNum > largestChainNum:
        largestChainNum = chainNum
        largestStartNum = i
print (largestStartNum, largestChainNum)
print ("Time elapsed", time.time()-start)
