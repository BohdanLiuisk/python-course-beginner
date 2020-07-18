n = int(input())

for i in range(1, n + 1):
    if n <= 9:
        for j in range(1, i + 1):
            print(j * 1, end="")
        print()
