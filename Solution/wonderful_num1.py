import math

for i in range(10, 100):
    if i == 2 * math.floor(i // 10) * (i % 10):
        print(i)
