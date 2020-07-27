writeFile = open("input.txt", "r", encoding="utf8")
i, nine = 0, 0
j, ten = 0, 0
k, eleven = 0, 0

for line in writeFile:
    if int(*[line.split()[2]]) == 9:
        nine += int(*[line.split()[3]])
        i += 1
    elif int(*[line.split()[2]]) == 10:
        ten += int(*[line.split()[3]])
        j += 1
    elif int(*[line.split()[2]]) == 11:
        eleven += int(*[line.split()[3]])
        k += 1

print(nine / i, ten / j, eleven / k)
