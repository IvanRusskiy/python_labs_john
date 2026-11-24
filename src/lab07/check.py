"""Проверка против эталона на случайных данных."""

from __future__ import annotations

import random

from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials: int = 100) -> None:
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(original), (
            f"{fn.__name__} ошиблась на {original}: получила {result}"
        )
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_search(trials: int = 100) -> None:
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = sorted(random.randint(-100, 100) for _ in range(n))

        # иногда берём существующий элемент, иногда — случайный
        if nums and random.random() < 0.5:
            target = random.choice(nums)
        else:
            target = random.randint(-100, 100)

        try:
            expected = nums.index(target)  # первый индекс (для linear)
        except ValueError:
            expected = -1

        linear = linear_search(nums, target)
        assert linear == expected, (
            f"linear_search ошиблась: nums={nums}, x={target}, "
            f"ожидали {expected}, получили {linear}"
        )

        binary = binary_search(nums, target)
        if expected == -1:
            assert binary == -1, (
                f"binary_search ошиблась: nums={nums}, x={target}, "
                f"ожидали -1, получили {binary}"
            )
        else:
            # бинарный поиск может вернуть любой индекс с этим значением
            assert 0 <= binary < len(nums) and nums[binary] == target, (
                f"binary_search ошиблась: nums={nums}, x={target}, "
                f"получили {binary}"
            )


def check_two_sum(trials: int = 100) -> None:
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        if n >= 2 and random.random() < 0.5:
            # гарантированно существует решение
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            while j == i:
                j = random.randint(0, n - 1)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-1000, 1000)

        r1 = two_sum_brute(nums, target)
        r2 = two_sum_fast(nums, target)

        # оба None или оба дают правильную сумму
        if r1 is None and r2 is None:
            continue
        if r1 is None or r2 is None:
            raise AssertionError(
                f"расхождение None: nums={nums}, target={target}, "
                f"brute={r1}, fast={r2}"
            )

        i1, j1 = r1
        i2, j2 = r2
        assert 0 <= i1 < j1 < len(nums)
        # fast может вернуть индексы в любом порядке
        assert nums[i1] + nums[j1] == target
        assert nums[i2] + nums[j2] == target


if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK: все проверки пройдены")
