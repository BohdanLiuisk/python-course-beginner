inFile = open('input.txt', 'r', encoding='utf8')
vocabulary = set()
vocList = set()
n = int(inFile.readline().strip())

for i in range(n):
    lLine = inFile.readline().strip()
    vocabulary.add(lLine)
    vocList.add(lLine.lower())

lLine = inFile.readline().split()
mistakes = 0

for i in lLine:
    if i.lower() in vocList and i not in vocabulary:
        mistakes += 1
    else:
        bLetters = 0
        for j in i:
            if j.isupper():
                bLetters += 1
        if bLetters != 1:
            mistakes += 1

print(mistakes)
inFile.close()
