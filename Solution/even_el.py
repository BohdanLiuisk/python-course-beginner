numList = list(map(int, input().split()))

for i in range(len(numList)):
    if numList[i] % 2 == 0:
        print(numList[i], end=" ")
