"""Поиск и Two Sum для ЛР7."""

from __future__ import annotations


def linear_search(nums: list, x) -> int:
    """Индекс первого вхождения x или -1."""
    for i, val in enumerate(nums):
        if val == x:
            return i
    return -1


def binary_search(sorted_nums: list, x) -> int:
    """Индекс x в отсортированном по возрастанию списке или -1.
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_sum_brute(nums: list, target: int) -> tuple[int, int] | None:
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums: list, target: int) -> tuple[int, int] | None:
    """То же, что two_sum_brute, но за один проход со словарём (значение → индекс)."""
    seen: dict[int, int] = {}
    for i, val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return (seen[complement], i)
        seen[val] = i
    return None
