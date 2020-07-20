numList = list(map(int, input().split()))
prevNum = numList[0]

for i in numList:
    if i > prevNum:
        print(i, end=' ')
    prevNum = i
