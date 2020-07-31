inFile = open('input.txt', 'r', encoding='utf8')
nm = list(map(int, inFile.readline().split()))
Anya = {int(inFile.readline().strip()) for i in range(nm[0])}
Boris = {int(inFile.readline().strip()) for i in range(nm[1])}

print(len(Anya & Boris))
print(*sorted(Anya & Boris))
print(len(Anya - Boris))
print(*sorted(Anya - Boris))
print(len(Boris - Anya))
print(*sorted(Boris - Anya))
