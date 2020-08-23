from itertools import permutations as prm


print(*map(''.join, prm(map(str, range(1, int(input())+1)))), sep='\n')
