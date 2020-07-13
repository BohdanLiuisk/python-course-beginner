def sqrt_only(flag=False):
    x = int(input())
    if x != 0:
        if sqrt_only(flag):
            flag = True
        if x ** 0.5 % 1 == 0:
            print(x, ' ', end='')
            flag = True
    return flag

if sqrt_only() is False:
    print('0')
