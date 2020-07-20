n = sorted(list(map(int, input().split())))

while n[0] <= 0:
    del n[0]
print(n[0])
