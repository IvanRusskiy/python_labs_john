"""Модуль конвертации CSV → XLSX (ЛР5).

Использует ensure_parent_dir из src.lab04.io_txt_csv (ЛР4).
Зависимость: openpyxl.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

# Добавляем корень репозитория в sys.path
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from src.lab04.io_txt_csv import ensure_parent_dir  # noqa: E402


def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    """
    Конвертирует CSV в XLSX.

    Использовать openpyxl.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    try:
        from openpyxl import Workbook
    except ModuleNotFoundError as err:
        if getattr(err, "name", None) != "openpyxl":
            raise
        raise RuntimeError(
            "Для создания XLSX установите openpyxl: python -m pip install openpyxl"
        ) from err

    source = Path(csv_path)
    target = Path(xlsx_path)

    if source.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался CSV-файл: {source}")
    if target.suffix.lower() != ".xlsx":
        raise ValueError(f"Ожидался XLSX-файл: {target}")

    if not source.exists():
        raise FileNotFoundError(f"Файл не найден: {source}")

    with source.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if not rows or not rows[0] or not any(str(v).strip() for v in rows[0]):
        raise ValueError("CSV пустой или не содержит заголовка")

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"

    for row in rows:
        sheet.append(row)

    # Автоширина колонок (минимум 8)
    for column in sheet.columns:
        column_letter = column[0].column_letter
        max_length = max(
            (len(str(cell.value)) if cell.value is not None else 0)
            for cell in column
        )
        sheet.column_dimensions[column_letter].width = max(8, max_length + 1)

    ensure_parent_dir(target)
    workbook.save(target)


if __name__ == "__main__":
    csv_to_xlsx(
        "data/lab05/samples/people.csv",
        "data/lab05/out/people.xlsx",
    )
    print("Конвертация CSV → XLSX выполнена.")
