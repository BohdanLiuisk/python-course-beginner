in_file = open('input.txt', 'r', encoding='utf8')
out_file = open('output.txt', 'w', encoding='utf8')
lst = []

for line in in_file:
    lst.append(line.split()[2:4])

class_9 = []
class_10 = []
class_11 = []

for element in lst:
    if int(element[0]) == 9:
        class_9.append(int(element[1]))
    elif int(element[0]) == 10:
        class_10.append(int(element[1]))
    elif int(element[0]) == 11:
        class_11.append(int(element[1]))

class_9.sort(reverse=True)
class_10.sort(reverse=True)
class_11.sort(reverse=True)

for i in class_9:
    if i < max(class_9):
        print(i, end=' ', file=out_file)
        break

for i in class_10:
    if i < max(class_10):
        print(i, end=' ', file=out_file)
        break

for i in class_11:
    if i < max(class_11):
        print(i, end=' ', file=out_file)
        break

in_file.close()
out_file.close()
