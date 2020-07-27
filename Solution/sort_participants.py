writeFile = open("input.txt", "r", encoding="utf8")
p = []

for line in writeFile:
    line = line.split()[0], line.split()[1], line.split()[3]
    p.append(line)

p.sort()

for i in p:
    print(*i)
