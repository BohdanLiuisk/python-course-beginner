n = int(input())

while(n > 10 ** 5):
    n = int(input())

array = list(map(int, input().split()[:n]))

print(*sorted(array))
