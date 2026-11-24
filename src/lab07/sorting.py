"""Сортировки для ЛР7. Каждая возвращает НОВЫЙ список, исходный не меняет."""

from __future__ import annotations


def bubble_sort(nums: list) -> list:
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
    Есть ранний выход, если обменов не было (★).
    """
    a = list(nums)          # обязательно копия
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:     # ранний выход
            break
    return a


def insertion_sort(nums: list) -> list:
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""
    a = list(nums)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(nums: list) -> list:
    """Новый список, отсортированный по возрастанию. Исходный не меняется."""
    a = list(nums)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
