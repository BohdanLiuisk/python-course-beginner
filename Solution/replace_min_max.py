a = [int(i) for i in input().split()]
max = a.index(max(a))
min = a.index(min(a))
if len(a) > 0:
    a[max], a[min] = a[min], a[max]
print(' '.join([str(i) for i in a]))
