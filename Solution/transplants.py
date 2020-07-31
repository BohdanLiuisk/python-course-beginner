n = list(map(int, input().split()))

terminal1 = sorted(set((n[0], n[1])))
terminal2 = sorted(set((n[-1], n[-2])))

bus1 = set(i for i in range(terminal1[0], int(terminal1[1])+1))
bus2 = set(i for i in range(terminal2[0], int(terminal2[1])+1))

print(len(bus1 & bus2))
