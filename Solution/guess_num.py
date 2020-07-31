inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
n = int(lines[0])
numbers = set([i for i in range(1, n + 1)])

for line in range(2, len(lines), 2):
    if lines[line] == 'YES\n':
        numSet = set(map(int, lines[line - 1].split()))
        numbers &= numSet
    elif lines[line] == 'NO\n':
        not_numbers = set(map(int, lines[line - 1].split()))
        numbers -= not_numbers

numbers = list(numbers)
numbers.sort()

print(*numbers)
