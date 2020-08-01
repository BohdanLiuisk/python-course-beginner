n = int(input())

tree = dict()

for i in range(n - 1):
    child, parent = input().split()
    tree[child] = parent

for name in sorted(list(set(list(tree.values()) + list(tree.keys())))):
    count = 0
    local_name = name

    while local_name in tree:
        count += 1
        local_name = tree[local_name]

    print(name, count)
