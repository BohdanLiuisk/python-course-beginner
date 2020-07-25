size = int(input())
s = sorted(map(int, input().split()))

c = 0
m = size - 3

for i in s:
    if i >= m + 3:
        c += 1
        m = i

print(c)
