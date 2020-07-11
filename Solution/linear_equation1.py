a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a != 0:
    y = (a * f - c * e) / (a * d - c * b)
    x = (e - b * ((a * f - c * e) / (a * d - c * b))) / a
elif a == 0:
    y = e / b
    x = (f - d * y) / c
print(x, y, sep=" ")
