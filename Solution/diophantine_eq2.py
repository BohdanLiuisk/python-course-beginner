a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
count_numbers = 0

for i in range(1001):
    if i != e:
        if (a * i ** 3 + b * i ** 2 + c * i + d) / (i - e) == 0:
            count_numbers += 1

print(count_numbers)
