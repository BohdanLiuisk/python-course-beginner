def keyCount(n, actualClicks, maxClicks):
    clickCount = [0] * n
    for click in actualClicks:
        clickCount[click - 1] += 1
    for i in range(n):
        if maxClicks[i] < clickCount[i]:
            print('YES')
        else:
            print('NO')

n = int(input())
maxClicks = [int(i) for i in input().split()]
k = int(input())
actualClicks = [int(i) for i in input().split()]

keyCount(n, actualClicks, maxClicks)
