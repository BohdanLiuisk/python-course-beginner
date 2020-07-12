def isPointInSquare(x, y):
    return -1 <= (x + y) <= 1 and -1 <= (x - y) <= 1 and -1 <= (y - x) <= 1

x, y = float(input()), float(input())
print('YES' if isPointInSquare(x, y) else 'NO')
