inFile = open('input.txt', 'r', encoding='utf8')
s = [0] * 12
m = [0] * 12

for line in inFile:
    l = line.split()
    m[int(l[2])] += 1
    if s[int(l[2])] < int(l[3]):
        s[int(l[2])] = int(l[3])

print(s[9], s[10], s[11])
inFile.close()
