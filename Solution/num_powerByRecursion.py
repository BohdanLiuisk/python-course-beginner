def power(a, n):
    if n > 1:
        a = a * power(a, n - 1)
    else:
        a = a ** n
    return a

a, n = float(input()), int(input())
print(power(a, n))
