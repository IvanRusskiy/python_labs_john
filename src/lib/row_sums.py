def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    возвращает сумму строк матрицы
    '''
    result = []
    len_str = []
    if mat == []:
        return 0
    for i in range(len(mat)):
        result.append(sum(mat[i]))
        len_str.append(len(mat[i]))
    if len(set(len_str)) != 1:
        raise ValueError("рваная матрица")
    return result