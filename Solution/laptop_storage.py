a1 = int(input())
b1 = int(input())
c1 = int(input())
x = int(input())
y = int(input())
z = int(input())

d1 = (a1 // x) * (b1 // y) * (c1 // z)
d2 = (a1 // x) * (c1 // y) * (b1 // z)
d3 = (b1 // x) * (c1 // y) * (a1 // z)
d4 = (b1 // x) * (a1 // y) * (c1 // z)
d5 = (c1 // x) * (a1 // y) * (b1 // z)
d6 = (c1 // x) * (b1 // y) * (a1 // z)

if d1 >= d2:
    d2 = d1
if d3 >= d4:
    d4 = d2
if d5 >= d6:
    d6 = d5

if d2 >= d4 and d2 >= d6:
    print(d2)
elif d4 >= d6:
    print(d4)
else:
    print(d6)
