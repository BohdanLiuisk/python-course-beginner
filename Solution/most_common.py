n = list(map(int, input().split()))
m = 0
count = 0
num = 0
more_than_one = False

for i in range(len(n)):
    count = n.count(n[i])
    if count > 0 and count > m:
        m = count
        num = n[i]
        more_than_one = True
if more_than_one is True:
    print(num)
