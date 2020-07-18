n = int(input())
card_sum = 0
num_sum = 0

for i in range(1, n):
    num = int(input())
    card_sum += num

for i in range(1, n + 1):
    num_sum += i

print(num_sum - card_sum)
