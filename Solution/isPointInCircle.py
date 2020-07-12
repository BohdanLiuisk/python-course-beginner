from math import pow


def isPointInCircle(x, y, xc, yc, r):
    return pow((x - xc), 2) + pow((y - yc), 2) <= pow(r, 2)

x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())

print('YES' if isPointInCircle(x, y, xc, yc, r) else 'NO')
