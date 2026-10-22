"""Модуль ввода/вывода для ЛР4: чтение текста и запись CSV.

Только стандартная библиотека. Функции чистые (без побочных эффектов,
кроме записи файла в write_csv / ensure_parent_dir).
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает файл целиком и возвращает его содержимое как одну строку.

    По умолчанию используется кодировка UTF-8.
    Чтобы прочитать файл в другой кодировке, передайте параметр, например:
        read_text("data/input.txt", encoding="cp1251")

    Ошибки FileNotFoundError и UnicodeDecodeError пробрасываются наверх —
    это ожидаемое поведение.

    Пустой файл → пустая строка.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские директории для path, если их ещё нет."""
    p = Path(path)
    parent = p.parent
    if parent and not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """Записывает CSV-файл с разделителем «,».

    - Если передан header — он пишется первой строкой.
    - Все строки в rows должны иметь одинаковую длину, иначе ValueError.
    - Пустой rows + header=None → пустой файл.
    - Пустой rows + header=("a", "b") → файл только с заголовком.

    Кодировка записи всегда UTF-8.
    """
    p = Path(path)
    ensure_parent_dir(p)

    rows_list = list(rows)

    if rows_list:
        expected_len = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != expected_len:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, "
                    f"ожидалась {expected_len}"
                )

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows_list:
            writer.writerow(row)
