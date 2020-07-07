n = int(input())
max = n
(i, m, j, k, h) = (1, 0, 0, 0, 0)
while n != 0:
    n = int(input())
    if n == 0:
        break
    i += 1
    if n > max:
        max = n
        m = i
    elif n < max:
        max = n
        k = i
    if k - m == 1 and j == 0:
        j = m
    if k - m == 1 and j != m and h == 0:
        h = m - j
        j = m
    if k - m == 1 and j != m and h != 0:
        if h > m - j:
            h = m - j
        j = m
print(h)
