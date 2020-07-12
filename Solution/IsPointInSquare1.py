def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1

x, y = float(input()), float(input())
print('YES' if IsPointInSquare(x, y) else 'NO')
