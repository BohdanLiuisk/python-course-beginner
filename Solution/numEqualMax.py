num = - 1
maxElement = 0
equalMax = 0
while num != 0:
    num = int(input())
    if num > maxElement:
        maxElement, equalMax = num, 1
    elif num == maxElement:
        equalMax += 1
print(equalMax)
