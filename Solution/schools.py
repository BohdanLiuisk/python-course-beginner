inFile = open('input.txt', 'r', encoding='utf8')
b = [0] * 100

for line in inFile:
    l = line.split()
    b[int(l[2])] += 1

mx = max(b)

for i in range(len(b)):
    if b[i] == mx:
        print(i, end=' ')
inFile.close()
