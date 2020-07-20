a = list(map(int, input().split()))
i = 0

while i <= len(a) - 1:
    j = i + 1
    l = len(a)
    while j < len(a):
        if a[i] == a[j]:
            a.pop(j)
        else:
            j += 1
    if len(a) < l:
        a.pop(i)
    else:
        i += 1

print(*a)
