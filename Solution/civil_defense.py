n = int(input())
sn = list(map(int, input().split()))
m = int(input())
sm = list(map(int, input().split()))
a = []
b = []
c = sn

for i in range(n):
    sn1 = (sn[i], i + 1)
    a.append(sn1)
for i in range(m):
    sm1 = (sm[i], i + 1)
    b.append(sm1)

a.sort()
b.sort()

i = 0
j = 0

while i < n and j < m - 1:
    if abs(a[i][0] - b[j][0]) <= abs(a[i][0] - b[j + 1][0]):
        c[a[i][1] - 1] = (b[j][1])
        i += 1
    else:
        j += 1
        if j == m - 1:
            while i < n:
                c[a[i][1] - 1] = (b[j][1])
                i += 1
        else:
            if abs(a[i][0] - b[j][0]) <= abs(a[i][0] - b[j + 1][0]):
                c[a[i][1] - 1] = (b[j][1])
                i += 1
if m == 1:
    for i in range(n):
        c[i] = 1

print(*c)
