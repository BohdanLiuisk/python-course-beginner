from decimal import Decimal
price = Decimal(input())
intPart = int(price)
fracPart = int(100 * (price - intPart))
print(intPart, fracPart)
