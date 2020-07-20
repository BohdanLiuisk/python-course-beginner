a = list(map(int, input().split()))
min_value = 0

for i in a:
    if i % 2 == 1:
        if min_value == 0:
            min_value = i
        else:
            if i < min_value:
                min_value = i
print(min_value)
