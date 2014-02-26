number=0
string = ''
while len(string) < 1000000:
    number += 1
    string += str(number)
prod = 1
for power in range(7):
    prod *= int(string[10**power-1])
print(prod)
