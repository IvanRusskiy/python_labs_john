def flatten(mat: list[list | tuple]) -> list:
    '''
    преобразует список списков в 1 список со значениями из внутренних списков
    '''
    result = []
    for l1st in mat:
        if type(l1st) != tuple and type(l1st) != list:
            raise TypeError("строка не строка строк матрицы")
        for n in l1st:
            result.append(n)
    return result
