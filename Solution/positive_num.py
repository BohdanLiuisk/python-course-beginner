numList = list(map(int, input().split()))
count = 0

for i in range(len(numList)):
    if numList[i] > 0:
        count += 1
print(count)
