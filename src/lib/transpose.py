def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    транспонирует матрицу
    '''
    if mat == []:
        return []
    transpose_matrix = [[0]*len(mat) for x in range(len(mat[0]))] 
    len_str = []
    for i in range(len(mat)):
        len_str.append(len(mat[i]))
        for j in range(len(mat[i])):
            transpose_matrix[j][i] = mat[i][j]
    if len(set(len_str)) != 1:
        raise ValueError("рваная матрица")
    return transpose_matrix