x = []
y = []
result = []

for i in range(8):
    n = list(map(int, input().split()))
    x.append(n[0])
    y.append(n[1])

for i in range(8):
    for j in range(i + 1, 8):
        if y[i] + abs(x[i] - x[j]) == y[j] or \
                y[i] - abs(x[i] - x[j]) == y[j]:
            result.append('YES')
        elif x[i] == x[j] or y[i] == y[j]:
            result.append('YES')
        else:
            result.append('NO')

if result.count('YES') != 0:
    print('YES')
else:
    print('NO')
