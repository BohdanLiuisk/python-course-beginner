p = {}
file = open('input.txt', 'r', encoding='utf8')

for l in file:
    a = l.split()
    p[a[0]] = p.get(a[0], 0) + int(a[1])
for x, z in sorted(p.items()):
    print(x, z)
