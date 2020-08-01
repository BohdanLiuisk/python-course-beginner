numNew = input()
num1 = input()
num2 = input()
num3 = input()
dictList = dict()
k = 0
myList = [numNew, num1, num2, num3]

for i in myList:
    tmp = ''
    k += 1
    for sym in i:
        if sym.isdigit():
            tmp += sym
    if len(tmp) == 7:
        tmp = '495' + tmp
    else:
        tmp = tmp[1:]
    dictList[k] = tmp
    if k >= 2:
        if dictList[1] == dictList[k]:
            print('YES')
        else:
            print('NO')
