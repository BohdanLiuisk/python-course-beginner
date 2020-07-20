def nearest_n(a, x):
    b = abs(max(a) - x)
    c = max(a)
    for i in a:
        if abs(i - x) <= b:
            c = i
            b = abs(i - x)
        else:
            continue
    return c

n = int(input())
a = list(map(int, input().split()))
x = int(input())
print(nearest_n(a, x))
