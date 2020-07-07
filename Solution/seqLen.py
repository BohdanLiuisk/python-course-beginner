n = int(input())
len = 0
while n > 0:
    len += 1
    n = int(input())
    if n == 0:
        continue
print(len)
