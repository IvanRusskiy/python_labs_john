"""CLI-конвертеры данных JSON / CSV / XLSX (ЛР6).

Подкоманды:
  json2csv  — JSON → CSV
  csv2json  — CSV → JSON
  csv2xlsx  — CSV → XLSX

Использует функции из src.lab05.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Добавляем корень репозитория в sys.path
_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from src.lab05.json_csv import json_to_csv, csv_to_json  # noqa: E402
from src.lab05.csv_xlsx import csv_to_xlsx  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Конвертеры данных JSON / CSV / XLSX"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --in сохраняем в поле input (in — зарезервированное слово)
    p1 = sub.add_parser(
        "json2csv",
        help="преобразовать JSON в CSV",
        description="Преобразует JSON в CSV.",
    )
    p1.add_argument("--in", dest="input", required=True, help="входной .json файл")
    p1.add_argument("--out", dest="output", required=True, help="выходной .csv файл")

    p2 = sub.add_parser(
        "csv2json",
        help="преобразовать CSV в JSON",
        description="Преобразует CSV в JSON.",
    )
    p2.add_argument("--in", dest="input", required=True, help="входной .csv файл")
    p2.add_argument("--out", dest="output", required=True, help="выходной .json файл")

    p3 = sub.add_parser(
        "csv2xlsx",
        help="преобразовать CSV в XLSX",
        description="Преобразует CSV в файл Excel.",
    )
    p3.add_argument("--in", dest="input", required=True, help="входной .csv файл")
    p3.add_argument("--out", dest="output", required=True, help="выходной .xlsx файл")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {args.input}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Ошибка: некорректный JSON", file=sys.stderr)
        sys.exit(1)
    except ValueError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as error:
        # Например, отсутствует openpyxl
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(1)

    print(f"Готово: {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
