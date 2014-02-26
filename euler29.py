import math
distinct = set()
for a in range(2, 101):
    for b in range(2,101):
        distinct.add(math.pow(a,b))
print (len(distinct))
