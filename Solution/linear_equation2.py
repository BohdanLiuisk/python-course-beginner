a, b, c, d, e, f = float(input()), float(input()), float(input()),\
                   float(input()), float(input()), float(input())
x = 0.0
y = 0.0
epsilon = 1e-6
if a != 0:
    if abs(a * d - b * c) < epsilon:
        if abs(a * f - c * e) < epsilon:
            if b == 0:
                x = e / a
                print('3', x)
            else:
                print('1', -a / b, e / b)
        else:
            print('0')
    else:
        y = (a * f - c * e) / (a * d - b * c)
        x = e / a - b / a * y
        print('2', x, y)
elif b != 0:
    # a = 0, b != 0
    y = e / b
    if c == 0:
        if d == 0:
            if f == 0:
                print('4', y)
            else:
                print('0')
        else:
            if abs(d * e - b * f) < epsilon:
                print('4', y)
            else:
                print('0')
    else:
        x = f / c - d / c * y
        print('2', x, y)
elif c != 0:
    # a = 0, b = 0, c != 0
    if e == 0:
        if d == 0:
            x = f / c
            print('3', x)
        else:
            print('1', -c / d, f / d)
    else:
        print('0')
elif d != 0:
    # a = 0, b = 0, c = 0
    if e == 0:
        y = f / d
        print('4', y)
    else:
        print('0')
else:
    # a = 0, b = 0, d = 0, c = 0
    if e == 0 and f == 0:
        print('5')
    else:
        print('0')
