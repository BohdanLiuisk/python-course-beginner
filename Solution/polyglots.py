import sys

sys.stdin = open("input.txt", 'r')
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    m = int(sys.stdin.readline())
    lst.append(set())
    for j in range(m):
        lst[i].add(sys.stdin.readline().strip())

tmp = lst[0].copy()

for i in range(1, len(lst)):
    tmp &= lst[i]

print(len(tmp), *tmp, sep='\n')
tmp = lst[0].copy()

for i in range(1, len(lst)):
    tmp |= lst[i]

print(len(tmp), *tmp, sep='\n')
