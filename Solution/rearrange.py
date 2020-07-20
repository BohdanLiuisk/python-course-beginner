numList = list(map(int, input().split()))
for i in range(len(numList) // 2):
    numList[i], numList[-i - 1] = numList[-i - 1], numList[i]
print(*numList)
