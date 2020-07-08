p = int(input())
x = int(input())
y = int(input())
moneyBefore = 100 * x + y
moneyAfter = int(moneyBefore * (100 + p) / 100)
print(moneyAfter // 100, moneyAfter % 100)
