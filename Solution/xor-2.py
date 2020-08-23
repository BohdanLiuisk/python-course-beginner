from functools import reduce


print(
    *map(
        lambda x: (reduce(lambda a, b: (a ^ b), x)),
        zip(*map(lambda x: map(int, input().split()), range(int(input()))))
    )
)
