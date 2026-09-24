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