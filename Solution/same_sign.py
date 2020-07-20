a = list(map(int, input().split()))
for i in range(1, len(a)):
    x = int(a[i - 1])
    y = int(a[i])
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        print(x, y)
        break
