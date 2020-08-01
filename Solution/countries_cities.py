with open('input.txt', 'r', encoding='utf8') as f:
    n = int(f.readline())
    lst, req = [], []
    for i in range(n):
        lst.append(f.readline().strip().split())
    m = int(f.readline())
    for j in range(m):
        req.extend(f.readline().strip().split())

cities = dict()
for i in range(len(lst)):
    for j in range(1, len(lst[i])):
        cities[lst[i][j]] = lst[i][0]

for now in req:
    print(cities[now])
