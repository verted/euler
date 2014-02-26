import euler
count = 0
for n in range(1,101):
    for r in range(1,n):
        if euler.comb(n,r)>1000000:
            count += 1
print (count)
