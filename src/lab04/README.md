# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

## Что сделано

- `src/lib/text.py` — модуль из ЛР3 (`normalize`, `tokenize`, `count_freq`, `top_n`)
- `src/lab04/io_txt_csv.py` — `read_text`, `write_csv`, `ensure_parent_dir`
- `src/lab04/text_report.py` — скрипт генерации отчётов (базовый + ★ несколько файлов)
- `data/lab04/` — тестовые файлы `input.txt`, `a.txt`, `b.txt`

## Запуск (из корня репозитория)

### Базовый режим (один файл)

```bash
python src/lab04/text_report.py
```

Читает `data/lab04/input.txt`, пишет `data/lab04/report.csv`.

Свои пути:

```bash
python src/lab04/text_report.py --in data/lab04/input.txt --out data/lab04/report.csv
```

Другая кодировка:

```bash
python src/lab04/text_report.py --in data/lab04/input.txt --encoding cp1251
```

### Режим нескольких файлов (★)

```bash
python src/lab04/text_report.py \
    --in data/lab04/a.txt data/lab04/b.txt \
    --per-file data/lab04/report_per_file.csv \
    --total data/lab04/report_total.csv
```

## Политики

| Случай | Поведение |
|--------|-----------|
| Пустой вход | `report.csv` содержит **только заголовок** `word,count` |
| Файл не найден | `FileNotFoundError` (пробрасывается) |
| Неверная кодировка | `UnicodeDecodeError` (пробрасывается) |
| Кодировка по умолчанию | UTF-8 (явно указывается при чтении/записи) |

## Пример вывода (базовый)

Вход `data/lab04/input.txt`:

![](https://github.com/IvanRusskiy/python_labs_john/blob/4624aa1f38e2019377ca06aa738a81ed0861ae90/images/lab04/io_txt_csv.png)

Консоль:

![](https://github.com/IvanRusskiy/python_labs_john/blob/4624aa1f38e2019377ca06aa738a81ed0861ae90/images/lab04/text_report1.png)

`data/lab04/report.csv`:

![](https://github.com/IvanRusskiy/python_labs_john/blob/4624aa1f38e2019377ca06aa738a81ed0861ae90/images/lab04/text_report2.png)

## Зависимости

Только стандартная библиотека Python 3.10+ (`csv`, `pathlib`, `argparse`, `collections`, `re`).
