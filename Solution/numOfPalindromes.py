k = int(input())
count = 0
for i in range(1, k + 1):
    str1 = str(i)
    if str1 == str1[:: - 1]:
        count += 1
print(count)
