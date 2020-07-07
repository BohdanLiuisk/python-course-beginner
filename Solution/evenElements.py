n = int(input())
evenElements = 0
while n != 0:
    if n % 2 == 0:
        evenElements += 1
    n = int(input())
print(evenElements)
