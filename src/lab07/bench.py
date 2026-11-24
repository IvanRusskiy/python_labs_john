"""Бенчмарк сортировок, поиска и Two Sum."""

from __future__ import annotations

import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def _time(stmt, number: int = 1) -> float:
    return timeit.timeit(stmt, number=number) / number


def run_bench() -> list[tuple]:
    random.seed(42)
    rows: list[tuple] = []

    # ---------- Сортировки ----------
    sizes = [1000, 10_000, 100_000]
    for n in sizes:
        data = [random.randint(-10**6, 10**6) for _ in range(n)]

        # sorted
        t = _time(lambda: sorted(data), number=3 if n <= 10_000 else 1)
        rows.append(("sort", n, "sorted", round(t, 6)))

        for name, fn in [
            ("bubble_sort", bubble_sort),
            ("insertion_sort", insertion_sort),
            ("selection_sort", selection_sort),
        ]:
            if n == 100_000:
                # квадратичные на 1e5 очень долго — ограничим
                rows.append(("sort", n, name, ">60"))
                continue
            t = _time(lambda fn=fn: fn(data), number=1 if n >= 10_000 else 3)
            rows.append(("sort", n, name, round(t, 6)))

    # ---------- Поиск ----------
    n = 100_000
    data = sorted(random.randint(-10**6, 10**6) for _ in range(n))
    queries = [random.choice(data) for _ in range(10_000)]  # 10k запросов

    t_lin = _time(lambda: [linear_search(data, q) for q in queries], number=1)
    rows.append(("search", n, "linear_search (10k queries)", round(t_lin, 6)))

    # время сортировки отдельно
    unsorted = list(data)
    random.shuffle(unsorted)
    t_sort = _time(lambda: sorted(unsorted), number=1)
    rows.append(("search", n, "sorted (для binary)", round(t_sort, 6)))

    t_bin = _time(lambda: [binary_search(data, q) for q in queries], number=1)
    rows.append(("search", n, "binary_search (10k queries)", round(t_bin, 6)))

    # ---------- Two Sum ----------
    for n in (1000, 10_000):
        data = [random.randint(-10**5, 10**5) for _ in range(n)]
        # гарантируем, что решение существует
        i, j = 0, 1
        target = data[i] + data[j]

        t_brute = _time(lambda: two_sum_brute(data, target), number=3 if n == 1000 else 1)
        rows.append(("two_sum", n, "two_sum_brute", round(t_brute, 6)))

        t_fast = _time(lambda: two_sum_fast(data, target), number=10)
        rows.append(("two_sum", n, "two_sum_fast", round(t_fast, 6)))

    return rows


def main() -> None:
    rows = run_bench()

    # красивая таблица в консоль
    print(f"{'task':<12} {'n':>8} {'impl':<35} {'seconds':>12}")
    print("-" * 70)
    for task, n, impl, sec in rows:
        print(f"{task:<12} {n:>8} {impl:<35} {sec:>12}")

    # запись в CSV
    out = Path("data/lab07/bench.csv")
    write_csv(
        rows,
        out,
        header=("task", "n", "impl", "seconds"),
    )
    print(f"\nРезультаты сохранены в {out}")


if __name__ == "__main__":
    main()
