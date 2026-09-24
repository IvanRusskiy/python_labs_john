def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''
    возвращает минимальное и максимальное значение в списке
    '''
    if nums == []: raise ValueError("пустой список")
    else:
        max = nums[0]
        min = nums[0]
        for i in nums:
            if i > max:
                max = i
            if i < min:
                min = i
    return min,max

# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5, 2, 2.0, -3.1]))
# print(min_max([]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''
    возвращает отсортированный список с неповторяющимися значениями
    '''
    if nums == []:
        return nums
    bigger0 = [i for i in nums if i > 0]
    lower0 = [i for i in nums if i < 0]
    sorted = [sum(lower0)-1,nums[0],sum(bigger0)+1]
    for num in nums:
        for j in range(len(sorted) - 1):
            if sorted[j] < num < sorted[j + 1]:
                sorted.insert(j + 1,num)
    sorted.remove(sorted[0])
    sorted.remove(sorted[-1])
    return sorted

# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

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

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
