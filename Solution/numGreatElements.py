num = int(input())
answer = 0
while num != 0:
    nextNum = int(input())
    if nextNum != 0 and num < nextNum:
        answer += 1
    num = nextNum
print(answer)
