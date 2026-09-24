def col_sums(h):
    if h == []:
        return 0
    l = [0]*len(h[0])
    k = []
    for i in h:
        k.append(len(i))
        for j in range(len(i)):
            l[j] += i[j]
    if len(set(k)) != 1:
        raise ValueError
    return l
