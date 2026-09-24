def row_sums(h):
    l = []
    j = []
    if h == []:
        return 0
    for i in range(len(h)):
        l.append(sum(h[i]))
        j.append(len(h[i]))
    if len(set(j)) != 1:
        raise ValueError
    return l