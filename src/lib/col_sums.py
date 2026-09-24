def col_sums(mat: list[list[float | int]]) -> list[float]:
    if mat == []:
        return 0
    result = [0]*len(mat[0])
    len_str = []
    for i in mat:
        len_str.append(len(i))
        for j in range(len(i)):
            result[j] += i[j]
    if len(set(len_str)) != 1:
        raise ValueError("рваная матрица")
    return result
