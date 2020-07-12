from math import sqrt


def isPrime(n):
    if n == 2:
        return 'YES'
    elif n % 2 == 0:
        return 'NO'
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return 'NO'
        i += 2
    return 'YES'

n = int(input())
print(isPrime(n))
