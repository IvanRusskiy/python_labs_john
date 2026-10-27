"""Модуль конвертации JSON ↔ CSV (ЛР5).

Использует ensure_parent_dir из src.lab04.io_txt_csv (ЛР4).
Чистые функции: только работа с файлами, без вывода в stdout.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

# Добавляем корень репозитория в sys.path
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from src.lab04.io_txt_csv import ensure_parent_dir  # noqa: E402


def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    """
    Преобразует JSON-файл в CSV.

    Поддерживает список словарей [{...}, {...}].
    Отсутствующие поля заполняются пустыми строками.
    Кодировка UTF-8.
    Порядок колонок — в порядке первого появления ключей.
    """
    source = Path(json_path)
    target = Path(csv_path)

    if source.suffix.lower() != ".json":
        raise ValueError(f"Ожидался файл с расширением .json: {source}")
    if target.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался файл с расширением .csv: {target}")

    if not source.exists():
        raise FileNotFoundError(f"Файл не найден: {source}")

    contents = source.read_text(encoding="utf-8")
    if not contents.strip():
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    data = json.loads(contents)

    if not isinstance(data, list) or not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if any(not isinstance(row, dict) for row in data):
        raise ValueError("Некорректные данные в JSON: ожидается список словарей")

    # Порядок колонок — по первому появлению ключей
    fieldnames: list[str] = list(
        dict.fromkeys(key for row in data for key in row.keys())
    )
    if not fieldnames:
        raise ValueError("В JSON нет полей для записи в CSV")

    ensure_parent_dir(target)

    with target.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in data:
            # отсутствующие ключи → пустая строка
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """
    Преобразует CSV в JSON (список словарей).

    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    source = Path(csv_path)
    target = Path(json_path)

    if source.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался файл с расширением .csv: {source}")
    if target.suffix.lower() != ".json":
        raise ValueError(f"Ожидался файл с расширением .json: {target}")

    if not source.exists():
        raise FileNotFoundError(f"Файл не найден: {source}")

    with source.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        if not fieldnames or not any(name and name.strip() for name in fieldnames):
            raise ValueError("CSV пустой или не содержит заголовка")

        if any(name is None or str(name).strip() == "" for name in fieldnames):
            raise ValueError("Заголовок CSV содержит пустое имя столбца")

        if len(set(fieldnames)) != len(fieldnames):
            raise ValueError("Заголовок CSV содержит повторяющиеся имена столбцов")

        rows = list(reader)

    ensure_parent_dir(target)

    with target.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Демонстрация (запуск из корня репозитория)
    json_to_csv(
        "data/lab05/samples/people.json",
        "data/lab05/out/people_from_json.csv",
    )
    csv_to_json(
        "data/lab05/samples/people.csv",
        "data/lab05/out/people_from_csv.json",
    )
    print("Конвертация JSON ↔ CSV выполнена.")
