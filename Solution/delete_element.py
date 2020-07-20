a = list(map(int, input().split()))
k = int(input())
a = a[:k] + a[k + 1:]
print(*a)
