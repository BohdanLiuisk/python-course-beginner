n = int(input())

f1 = '+___ '
f2 = ''
f3 = '|__\ '
f4 = '|    '
for i in range(n):
    f2 = f2 + '|' + str(i+1) + ' / '

fx = f1 * n, f2, f3 * n, f4 * n
print(*fx, sep='\n')
