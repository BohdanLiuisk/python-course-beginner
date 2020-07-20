n = list(map(int, input().split()))
count = 0

for i in range(len(n)):
    for k in range(i + 1, len(n)):
        if n[i] == n[k]:
            count += 1

print(count)
