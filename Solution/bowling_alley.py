nums = list(map(int, input().split()))
skittle = list()

for i in range(nums[0]):
    skittle.append('I')
for i in range(nums[1]):
    from_skittle, before_skittle = [int(from_skittle) for
                                    from_skittle in input().split()]
    for j in range(from_skittle - 1, before_skittle):
        del skittle[j]
        skittle.insert(j, '.')

print(*skittle, sep='')
