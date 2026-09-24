def min_max(h):
    if h == []: raise ValueError
    else:
        a = h[0]
        b = h[0]
        for i in h:
            if i > a:
                a = i
            if i < b:
                b = i
    return b,a