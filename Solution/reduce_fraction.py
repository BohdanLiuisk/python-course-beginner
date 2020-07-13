def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def ReduceFraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)

n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
