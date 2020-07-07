a = int(input())
b = int(input())
max = 1
n = 1
while 0 == 0:
    if b == 0 or a == 0:
        break
    while a > b:
        if b == 0:
            break  
        n += 1
        if n > max:
            max = n
            a = b
            b = int(input())
        else:
            a = b
            b = int(input())
    n = 1
    while a < b:
        n += 1
        if n > max:
            max = n
            a = b
            b = int(input())
        else:
            a = b
            b = int(input())
    n = 1
    while a == b:
        n = 1
        a = b
        b = int(input())
print(max)
