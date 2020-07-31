inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
n = int(lines[0])
numbers = set([i for i in range(1, n + 1)])

for line in range(1, len(lines) - 1):
    question = set(map(int, lines[line].split()))
    if len(question & numbers) <= len(numbers) // 2:
        print('NO')
        numbers -= question
    elif len(question & numbers) > len(numbers) // 2:
        print('YES')
        numbers &= question

numbers = list(numbers)
numbers.sort()

print(*numbers)
