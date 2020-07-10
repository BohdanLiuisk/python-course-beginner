from math import sqrt

partial_sum = 0
partial_sum_sqrt = 0
x = int(input())
n = 0
while x != 0:
    n += 1
    partial_sum += x
    partial_sum_sqrt += x ** 2
    x = int(input())
print(sqrt((partial_sum_sqrt - partial_sum ** 2 / n) / (n - 1)))
