def transpose(h):
    if h == []:
        return []
    a = len(h)
    b = len(h[0])
    g = [[0]*a for x in range(b)] 
    l = []
    for i in range(len(h)):
        l.append(len(h[i]))
        for j in range(len(h[i])):
            g[j][i] = h[i][j]
    if len(set(l)) != 1:
        raise ValueError
    return g

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

h = []
print(col_sums(h))