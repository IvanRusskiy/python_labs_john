def bubble_sort(nums) -> list:
    count = 0
    flag = 0 
    index = 0
    while flag != 1:
        for i in range(0,len(nums) - 1 - index):
            if nums[i] > nums[i + 1]:
                el = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = el
                count += 1
        index += 1
        if count == 0:
            flag = 1
        count = 0
    return nums

def insertion_sort(nums: list) -> list:
    for i in range(1,len(nums)):
        el = nums[i]
        j = i - 1
        while j >= 0 and el < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = el 
    return nums

def selection_sort(nums) -> list:
    n = len(nums)
    for i in range(n):
        min = i
        for j in range(i,n):
            if nums[j] < nums[i]:
                min = j
        nums[min],nums[i] = nums[i],nums[min]
    return nums


print(selection_sort([2,1,4,302408,3,398,9274,945,93]))