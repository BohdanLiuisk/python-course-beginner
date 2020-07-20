a = list(map(int, input().split()))
index, element = map(int, input().split())

b = a[:index]
v = a[index:]
b.append(element)
b = b + v

print(*b)
