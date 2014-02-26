prods = []
for m in range(10,100):
    for n in range(m+1,100):
        for i in range(len(str(m))):
            for j in range(len(str(n))):
                if str(m)[i] == str(n)[j] and str(m)[i] != '0':
                    if int(str(n)[0 if j else 1]) != 0 and int(str(m)[0 if i else 1])/int(str(n)[0 if j else 1]) == m/n:
                        prods.append(m/n)
                        print(m,n, int(str(m)[0 if i else 1]),int(str(n)[0 if j else 1]))
total = 1
for prod in prods:
    total *= prod
print(total)
