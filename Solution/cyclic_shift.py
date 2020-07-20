lst = list(map(int, input().split()))

for i in range(len(lst)):
    lst[i], lst[-1] = lst[- 1], lst[i]

print(*lst)
