from sorting import *
import random
def check_sorting(fn, trials=100) -> None:
    for _ in range(trials):
        n = random.randint(0,50)
        nums = [random.randint(-100,100) for o in range(n)]
        nums1 = nums.copy()
        nums = fn(nums)
        sort = sorted(nums1)
        if nums != sort:
            raise AssertionError

from search import *
def check_search(trials=100) -> None:
    for _ in range(trials):
        n = random.randint(0,50)
        nums = sorted([random.randint(-100,100) for o in range(n)])
        if random.randint < 0.5:
            target = random.choice(nums)
        else:
            target = random.randint(-100,100)
        try:
            index_search = nums.index(target)
        except:
            index_search = -1
        linear = linear_search(nums)
        if index_search != linear:
            raise AssertionError
        binary = binary_search(nums)
        if index_search != binary:
            raise AssertionError

def check_two_sum(trials=100) -> None:
    for _ in range(trials):
        n = random.randint(0,50)
        nums = [random.randint(-100,100) for o in range(n)]
        if random.randint < 0.5:
            target = random.choice(nums) + random.choice(nums)
        else:
            target = random.randint(-1000,1000)
        result1 = two_sum_brute(nums,target)
        result2 = two_sum_fast(nums,target)
        if result1 != result2:
            raise AssertionError
