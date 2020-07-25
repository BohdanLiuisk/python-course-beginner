arr = list(map(int, input().split()))
usr_data = [int(input()) for _ in range(arr[1])]
used_space, qty = 0, 0

for i in range(arr[1]):
    used_space += min(usr_data)
    usr_data.pop(usr_data.index(min(usr_data)))
    if used_space <= arr[0]:
        qty += 1

print(qty)
