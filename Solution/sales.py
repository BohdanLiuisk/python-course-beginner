bill = dict()

with open('input.txt', 'r', encoding='utf8') as shop:
    for i in shop:
        buyer = i.split()
        if buyer[0] not in bill:
            bill[buyer[0]] = dict()
        if buyer[1] not in bill[buyer[0]]:
            bill[buyer[0]][buyer[1]] = 0
        bill[buyer[0]][buyer[1]] += int(buyer[2])
for i in sorted(bill):
    print(i + ':')
    for j in sorted(bill[i]):
        print(j, bill[i][j])
