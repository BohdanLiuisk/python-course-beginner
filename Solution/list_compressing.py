lsn = list(map(int, input().split()))
k = 0
i = 0

while i <= (len(lsn) - 1):
    if lsn[i] != 0:
        print(lsn[i], end=' ')
        i += 1
    else:
        lsn.pop(i)
        k += 1

print('0 ' * k, end=' ')
