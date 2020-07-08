from math import sqrt

side1 = float(input())
side2 = float(input())
side3 = float(input())
p = (side1 + side2 + side3) / 2
area = sqrt(p * (p - side1) * (p - side2) * (p - side3))
print(area)
