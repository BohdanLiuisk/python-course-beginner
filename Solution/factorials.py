import itertools


print(1, *itertools.accumulate(map(int, range(1, 1 + int(input()))), lambda x, y: x * y))
