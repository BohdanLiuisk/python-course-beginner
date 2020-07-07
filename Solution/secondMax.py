firstMax = int(input())
secondMax = int(input())
if firstMax < secondMax:
    firstMax, secondMax = secondMax, firstMax
element = int(input())
while element != 0:
    if element > firstMax:
        secondMax, firstMax = firstMax, element
    elif element > secondMax:
        secondMax = element
    element = int(input())
print(secondMax)
