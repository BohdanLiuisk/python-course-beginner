a = list(map(int, input().split()))
b = a[:]

imax1 = a.pop(a.index(max(a)))
imax2 = a.pop(a.index(max(a)))
imin1 = b.pop(b.index(min(b)))
imin2 = b.pop(b.index(min(b)))

if imax1 * imax2 >= imin1 * imin2:
    print(min(imax1, imax2), max(imax1, imax2))
else:
    print(min(imin1, imin2), max(imin1, imin2))
