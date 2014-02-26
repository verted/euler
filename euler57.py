count = 0
numerator = 1
denominator = 1
for i in range(1000):
    temp = denominator*2
    denominator+=numerator
    numerator += temp
    if len(str(numerator))> len(str(denominator)):
        count += 1
print(count)
