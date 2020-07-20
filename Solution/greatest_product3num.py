a = list(map(int, input().split()))
b = a[:]

maxi1 = a.pop(a.index(max(a)))
maxi2 = a.pop(a.index(max(a)))
maxi3 = a.pop(a.index(max(a)))
mini1 = b.pop(b.index(min(b)))
mini2 = b.pop(b.index(min(b)))

if maxi1 * maxi2 * maxi3 >= maxi1 * mini1 * mini2:
    print(maxi1, maxi2, maxi3)
else:
    print(maxi1, mini1, mini2)
