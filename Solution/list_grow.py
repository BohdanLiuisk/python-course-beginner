def isAscending(numList):
    i = 0
    while i < len(numList) - 1:
        if int(numList[i]) >= int(numList[i + 1]):
            return 'NO'
        i += 1
    return 'YES'

numList = input().split()
print(isAscending(numList))
