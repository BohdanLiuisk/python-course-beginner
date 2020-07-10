from math import sqrt

a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c

if a == 0 and b == 0 and c != 0:
    print('0')
elif a == b == c == 0:
    print('3')
elif a == 0:
    print('1', -c / b)
elif D == 0:
    x = (-b + sqrt(D)) / (2 * a)
    print('1', x)
elif D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    if x1 < x2:
        print('2', x1, x2)
    else:
        print('2', x2, x1)
elif D < 0:
    print('0')
