def flatten(h):
    j = []
    for i in h:
        for x in i:
            j.append(x)
            if str(x) == x:
                raise TypeError
    return j
