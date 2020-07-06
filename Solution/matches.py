l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
cross12 = l1 <= r2 and l2 <= r1
cross13 = l1 <= r3 and l3 <= r1
cross23 = l2 <= r3 and l3 <= r2
if cross12 + cross13 + cross23 >= 2:
    print(0)
elif 0 < l3 - r2 <= r1 - l1 or 0 < l2 - r3 <= r1 - l1 or cross23:
    print(1)
elif 0 < l3 - r1 <= r2 - l2 or 0 < l1 - r3 <= r2 - l2 or cross13:
    print(2)
elif 0 < l2 - r1 <= r3 - l3 or 0 < l1 - r2 <= r3 - l3 or cross12:
    print(3)
else:
    print(-1)
