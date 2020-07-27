km = list(map(int, input().split()))
tarif = list(map(int, input().split()))
pay = 0
km.sort()
tarif.sort(reverse=True)

for i in range(len(km)):
    pay += km[i] * tarif[i]

print(pay)
