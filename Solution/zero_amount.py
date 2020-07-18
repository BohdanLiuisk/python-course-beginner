n = int(input())
zero_sum = 0

while n > 0:
    num = int(input())
    if num == 0:
        zero_sum += 1
    n -= 1

print(zero_sum)
