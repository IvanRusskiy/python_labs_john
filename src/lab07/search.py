def linear_search(nums, x) -> int:
    for i in range(0,len(nums)):
        if nums[i] == x:
            return i
    else:
        return -1

def binary_search(sorted_nums, x) -> int:
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid +1
        elif sorted_nums[mid] > x:
            hi = mid - 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    n = len(nums)
    for i in range(0,n):
        for j in range(i + 1,n):
            if nums[i] + nums[j] == target:
                return (i,j)
    return None

def two_sum_fast(nums, target) -> tuple[int, int] | None:
    seen = set()
    for n in nums:
        complement = target - n
        if complement in seen:
            return (complement, n)
        seen.add(n)
    return None
