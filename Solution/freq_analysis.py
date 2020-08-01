words, n, myList = {}, [], []
file = open('input.txt', encoding='utf8')

for line in file:
    n.extend(line.split())
for i in n:
    words[i] = words.get(i, 0) + 1
for word, num in words.items():
    myList.append((num, word))

myList.sort(key=lambda x: (-x[0], x[1]))

for i in range(len(myList)):
    print(myList[i][1])
