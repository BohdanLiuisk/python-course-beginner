n = int(input())
m = 0
a = 0
while n > 0:
    a = n % 10
    n = n // 10
    m = m * 10 + a
print(m)
