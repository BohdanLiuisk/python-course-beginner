fil = open('input.txt', 'r', encoding='utf8')
n = int(fil.readline())
results = []

for line in fil:
    spl = line.split()
    results.append((spl[0], int(spl[1])))

results.sort(key=lambda x: x[1], reverse=True)
foot = open('output.txt', 'w', encoding='utf8')

print('\n'.join([x[0] for x in results]), file=foot)
foot.close()
