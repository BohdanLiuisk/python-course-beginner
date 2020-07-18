n = int(input())
maxNum = 10 ** n - 1
minNum = 10 ** (n - 1)
for i in range(maxNum, minNum - 1, -2):
    print(i, end=' ')
