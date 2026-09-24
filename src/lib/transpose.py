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