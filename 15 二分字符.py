def bin_seq2(n):
    res = []
    for i in range(2 ** n):
        bin_2 = bin(i)[2:].zfill(n)
        if i & (i << 1) == 0:
            res.append(bin_2)
    return res

print(bin_seq2(8))