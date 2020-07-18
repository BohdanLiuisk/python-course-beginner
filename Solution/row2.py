a, b = int(input()), int(input())

if a < b:
    for i in range(a - 1, b):
        print(i + 1, end=" ")
else:
    for i in range(a + 1, b, -1):
        print(i - 1, end=" ")
