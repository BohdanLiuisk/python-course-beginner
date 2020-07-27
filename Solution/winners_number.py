kls = dict()
with open('input.txt', encoding='utf-8') as file:
    for line in file:
        s = line.strip().split()
        kls[int(s[-2])] = kls.get(int(s[-2]), []) + [int(s[-1])]
print(*[kls[key].count(max(kls[key])) for key in sorted(kls.keys())])
