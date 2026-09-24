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

# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
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

# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

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

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))