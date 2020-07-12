def xor(x, y):
    return int(x + y == 1)

x, y = int(input()), int(input())
print('1' if xor(x, y) else '0')
