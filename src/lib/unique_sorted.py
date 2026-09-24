def unique_sorted(h):
    if h == []:
        return []
    j = [h[0]]
    for i in h:
        if i in j:
            continue
        else:
            j.append(i)
    return sorted(j)