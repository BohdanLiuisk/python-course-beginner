l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())

good1_2 = (lc >= l1 + l2) and (wc >= w1) and (wc >= w2)
good1_3 = (lc >= l1 + w2) and (wc >= w1) and (wc >= l2)
good1_4 = (lc >= w1 + w2) and (wc >= l1) and (wc >= l2)
good1_5 = (lc >= w1 + l2) and (wc >= w2) and (wc >= l1)
good1_6 = (wc >= l1 + l2) and (lc >= w1) and (lc >= w2)
good1_7 = (wc >= l1 + w2) and (lc >= w1) and (lc >= l2)
good1_8 = (wc >= w1 + w2) and (lc >= l1) and (lc >= l2)
good1_9 = (wc >= w1 + l2) and (lc >= w2) and (lc >= l1)
good2_2 = (lc >= l1) and (wc >= w1)
good2_3 = (lc >= l2) and (wc >= w2)
good2_4 = (lc >= w1) and (wc >= l1)
good2_5 = (lc >= w2) and (wc >= l2)
if (hc < h1) or (hc < h2):
    print('NO')
elif ((good2_2 or good2_4) and (good2_3 or good2_5)):
    if hc >= (h1 + h2):
        print('YES')
    elif (good1_2 or good1_3 or good1_4 or good1_5):
        print('YES')
    elif (good1_6 or good1_7 or good1_8 or good1_9):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
