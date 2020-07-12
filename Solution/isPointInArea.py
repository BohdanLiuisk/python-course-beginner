def isPointInArea(a, b):
    k = ((-1 - a) ** 2 + (1 - b) ** 2) ** (1 / 2)
    l1 = b + a
    l2 = 2 * a + 2 - b
    v = (k <= 2) and (l1 >= 0) and (l2 <= 0)
    n = (k >= 2) and (l1 <= 0) and (l2 >= 0)
    return v or n

x, y = float(input()), float(input())
print('YES' if isPointInArea(x, y) else 'NO')
