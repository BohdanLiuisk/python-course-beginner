s = input()
i = 0
count = 1
while i <= len(s) - 1:
    if s[i] == " ":
        count += 1
    i += 1
print(count)
