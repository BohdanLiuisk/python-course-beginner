k = int(input())
m = int(input())
n = int(input())
if 2 * n % k == 0 and n > k:
    t = (n * 2 // k) * m
else:
    if n % k != 0 and k < n:
        t = (n * 2 // k) * m + m
    else:
        if n <= k:
            t = 2 * m
print(t)
