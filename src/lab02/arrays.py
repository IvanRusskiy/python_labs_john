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

def flatten(h):
    j = []
    for i in h:
        for x in i:
            j.append(x)
            if str(x) == x:
                return 1
    return j

h = [[1, 2], "ab"]
print(flatten(h))
print(str(object) in [1,'a'])