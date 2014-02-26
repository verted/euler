import math
import time
import string
start = time.time()
chrValues = {}
letters = string.ascii_uppercase
for i in range(len(letters)):
    chrValues[letters[i]] = i + 1
f = open("words.txt")
fileInput = f.read()
f.close()
fileInput = fileInput.replace("\"", "")
words = fileInput.split(",")
triCount = 0
for word in words:
    wordSum = 0
    for c in word:
        wordSum += chrValues[c]
    if 8*wordSum + 1 ** 1/2 %1 == 0:
        triCount +=1 
print(time.time()- start)
