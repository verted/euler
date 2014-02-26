import string
allTheLetters = string.ascii_lowercase
letterValue = {}
for i in range(len(allTheLetters)):
    letterValue[allTheLetters[i]] = i+1
f = open('names.txt')
names = f.read()
names = names.replace("\"","")
names = names.split(",")
f.close()
allScore = 0
pos = 1
for name in sorted(names):
    currScore = 0
    for letter in name.lower():
        currScore += letterValue[letter]
    allScore += currScore*pos
    pos+=1
print(allScore)
