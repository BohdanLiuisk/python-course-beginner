i = list(i for i in map(int, input().split()))
print(max(i), len(i) - i[::-1].index(max(i)) - 1)
