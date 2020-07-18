def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
factorial_sum = 0

for i in range(1, n + 1):
    factorial_sum += factorial(i)

print(factorial_sum)
