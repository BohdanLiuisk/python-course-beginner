winner = open('output.txt', 'w', encoding='utf8')
students = open('input.txt', 'r', encoding='utf8')
more_40 = []

for line in students:
    line = line.split()
    if len(line) == 1:
        k = int(line[0])
    elif int(line[-1]) >= 40 and int(line[-2]) >= 40 and int(line[-3]) >= 40:
        b = int(line[-1]) + int(line[-2]) + int(line[-3])
        more_40.append(b)

more_40.sort(key=lambda p: -p)
ans = 1

if len(more_40) > k:
    for now in more_40:
        if now > more_40[k]:
            ans = now
    print(ans, file=winner)
elif len(more_40) <= k:
    print('0', file=winner)
