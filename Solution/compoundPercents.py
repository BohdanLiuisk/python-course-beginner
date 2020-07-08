p, x, y, year = int(input()), int(input()), int(input()), int(input())
sum = x * 100 + y
while year > 0:
    sum += int(p / 100 * sum)
    year -= 1
print(int(sum // 100), int(sum % 100))
