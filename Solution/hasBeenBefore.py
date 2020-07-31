a = list(map(int, input().split()))
b = [0] * (len(a) + 1)

for i in a:
    b[i] += 1
    if b[i] >= 2:
        print("YES")
    else:
        print("NO")
