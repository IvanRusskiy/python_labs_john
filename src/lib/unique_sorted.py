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