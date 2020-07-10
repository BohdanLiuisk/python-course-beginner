n = int(input())
x = float(input())
coef = float(input())
result = coef
for i in range(0, n):
    coef = float(input())
    result *= x
    result += coef
print(result)
