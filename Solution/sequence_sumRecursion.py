def seq_sum():
    n = int(input())
    if n == 0:
        return 0
    return n + seq_sum()

print(seq_sum())
