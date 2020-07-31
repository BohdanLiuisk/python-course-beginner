inFile = open('input.txt', 'r', encoding='utf8')

lines = inFile.readlines()
lineFirst = list(map(int, lines[0].split()))
days, numParties = lineFirst[0], lineFirst[1]
dayFirst = []
dayStep = []

for i in range(1, 1 + numParties):
    line = list(map(int, lines[i].split()))
    dayFirst.append(line[0])
    dayStep.append(line[1])

strikeDays = set()

for j in range(numParties):
    strikeDays |= set(i for i in range(dayFirst[j], days + 1, dayStep[j]))

sundays = set(i for i in range(6, days + 1, 7))
saturdays = set(i for i in range(7, days + 1, 7))

strikeDays -= sundays
strikeDays -= saturdays

print(len(strikeDays))
