#!/usr/bin/env python3
"""Генерация CSV-отчётов по частотам слов (ЛР4).

Базовый режим (один файл):
    python src/lab04/text_report.py
    python src/lab04/text_report.py --in data/lab04/input.txt --out data/lab04/report.csv

Режим нескольких файлов (★):
    python src/lab04/text_report.py \\
        --in data/lab04/a.txt data/lab04/b.txt \\
        --per-file data/lab04/report_per_file.csv \\
        --total data/lab04/report_total.csv

Политика пустого входа: report.csv содержит только заголовок word,count.
Ошибки чтения (нет файла / неверная кодировка) пробрасываются.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

# Добавляем корень репозитория в sys.path, чтобы работали импорты
# как из VS Code, так и при запуске из любой директории.
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from src.lib.text import normalize, tokenize, count_freq, top_n  # noqa: E402
from src.lab04.io_txt_csv import read_text, write_csv  # noqa: E402


def frequencies_from_text(text: str) -> dict[str, int]:
    """Считает частоты слов после normalize + tokenize."""
    tokens = tokenize(normalize(text))
    return count_freq(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортировка: count ↓, word ↑."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def print_summary(freq: dict[str, int], total_tokens: int) -> None:
    """Краткое резюме в консоль + топ-5."""
    print(f"Всего слов: {total_tokens}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, cnt in top_n(freq, 5):
        print(f"{word}:{cnt}")


def print_pretty_table(rows: list[tuple[str, int]], title: str = "слово") -> None:
    """Красивая таблица (★): ширина столбца по максимуму."""
    if not rows:
        return
    col1 = title
    col2 = "частота"
    w1 = max(len(col1), max(len(w) for w, _ in rows))
    w2 = max(len(col2), max(len(str(c)) for _, c in rows))
    print(f"{col1:<{w1}} | {col2}")
    print("-" * (w1 + 3 + w2))
    for word, cnt in rows:
        print(f"{word:<{w1}} | {cnt}")


def process_single(
    in_path: Path,
    out_path: Path,
    encoding: str,
    pretty: bool = True,
) -> None:
    """Обработка одного файла → report.csv + резюме в консоль."""
    text = read_text(in_path, encoding=encoding)
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    rows = sorted_word_counts(freq)

    write_csv(rows, out_path, header=("word", "count"))
    print_summary(freq, len(tokens))

    if pretty and rows:
        print()
        print_pretty_table(rows[:10])  # топ-10 для наглядности


def process_multiple(
    in_paths: list[Path],
    per_file_path: Path,
    total_path: Path,
    encoding: str,
) -> None:
    """Несколько файлов → report_per_file.csv + report_total.csv."""
    per_file_rows: list[tuple[str, str, int]] = []
    total_counter: Counter[str] = Counter()

    for path in in_paths:
        text = read_text(path, encoding=encoding)
        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)
        total_counter.update(freq)

        # имя файла без полного пути — как в примере (a.txt, b.txt)
        name = path.name
        for word, cnt in sorted_word_counts(freq):
            per_file_rows.append((name, word, cnt))

    # сортировка: file ↑, count ↓, word ↑
    per_file_rows.sort(key=lambda r: (r[0], -r[2], r[1]))

    write_csv(per_file_rows, per_file_path, header=("file", "word", "count"))
    write_csv(
        sorted_word_counts(dict(total_counter)),
        total_path,
        header=("word", "count"),
    )

    print(f"Обработано файлов: {len(in_paths)}")
    print(f"Сводный отчёт: {total_path}")
    print(f"Отчёт по файлам: {per_file_path}")
    print()
    print_summary(dict(total_counter), sum(total_counter.values()))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Генерация CSV-отчётов по частотам слов (ЛР4)"
    )
    p.add_argument(
        "--in",
        dest="inputs",
        nargs="+",
        default=["data/lab04/input.txt"],
        help="Входной файл(ы). По умолчанию: data/lab04/input.txt",
    )
    p.add_argument(
        "--out",
        default="data/lab04/report.csv",
        help="Выходной CSV для одного файла (по умолчанию data/lab04/report.csv)",
    )
    p.add_argument(
        "--encoding",
        default="utf-8",
        help="Кодировка входных файлов (по умолчанию utf-8). Пример: cp1251",
    )
    p.add_argument(
        "--per-file",
        default=None,
        help="Путь для отчёта по каждому файлу (★). Если указан — включается режим нескольких файлов",
    )
    p.add_argument(
        "--total",
        default="data/lab04/report_total.csv",
        help="Путь для сводного отчёта (★). По умолчанию data/lab04/report_total.csv",
    )
    p.add_argument(
        "--no-pretty",
        action="store_true",
        help="Не печатать красивую таблицу",
    )
    return p


def main() -> None:
    args = build_parser().parse_args()
    inputs = [Path(x) for x in args.inputs]

    if args.per_file is not None or len(inputs) > 1:
        # Режим нескольких файлов
        per_file = Path(args.per_file or "data/lab04/report_per_file.csv")
        total = Path(args.total)
        process_multiple(inputs, per_file, total, args.encoding)
    else:
        # Базовый режим — один файл
        process_single(
            inputs[0],
            Path(args.out),
            args.encoding,
            pretty=not args.no_pretty,
        )


if __name__ == "__main__":
    main()
