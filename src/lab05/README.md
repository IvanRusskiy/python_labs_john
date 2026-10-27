# ЛР5 — JSON и конвертации (JSON↔CSV, CSV→XLSX)

> **Цель:** разобраться с форматом JSON, сериализацией/десериализацией и табличными конвертациями.  
> **Связь:** продолжение ЛР4 (работа с файлами) и подготовка базы для ЛР6 (CLI-конвертеры) и ЛР7 (тестирование).

В модулях переиспользуется `ensure_parent_dir` из `src/lab04/io_txt_csv.py` (ЛР4).

---

## Результат

- `src/lab05/json_csv.py` — чистые функции:
  - `json_to_csv(json_path, csv_path)`
  - `csv_to_json(csv_path, json_path)`
- `src/lab05/csv_xlsx.py` — функция `csv_to_xlsx(csv_path, xlsx_path)` (через **openpyxl**, авто-ширина колонок)
- Примеры данных в `data/lab05/samples/` и результаты в `data/lab05/out/`
- `requirements.txt` с зависимостью `openpyxl`

Всё остальное — стандартная библиотека (`json`, `csv`, `pathlib`).

---

## Структура

```
python_labs/
├─ requirements.txt
├─ src/
│  ├─ lib/
│  │  └── text.py              # из ЛР3
│  ├─ lab04/
│  │  └── io_txt_csv.py        # read_text, write_csv, ensure_parent_dir (ЛР4)
│  └─ lab05/
│     ├── json_csv.py          # JSON ↔ CSV
│     ├── csv_xlsx.py          # CSV → XLSX
│     ├── __init__.py
│     └── README.md
├─ data/
│  └─ lab05/
│     ├── samples/
│     │  ├── people.json
│     │  ├── people.csv
│     │  └── cities.csv
│     └── out/
│        ├── people_from_json.csv
│        ├── people_from_csv.json
│        └── people.xlsx
└─ ...
```

---

## Зависимость

```bash
python -m pip install -r requirements.txt
# или
python -m pip install openpyxl
```

---

## Задание A — JSON ↔ CSV
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab05/json%3C-%3Ecsv.png)
### `json_to_csv(json_path, csv_path)`

- Читает непустой JSON-массив словарей.
- Собирает столбцы по ключам **в порядке первого появления**.
- Отсутствующие поля → пустые ячейки.
- Кодировка UTF-8.

### `csv_to_json(csv_path, json_path)`

- Читает CSV с обязательным заголовком.
- Сохраняет строки как список словарей.
- Значения остаются строками.
- `json.dump(..., ensure_ascii=False, indent=2)`.

### Запуск (из корня репозитория)

```bash
python -c "
from src.lab05.json_csv import json_to_csv, csv_to_json
json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')
csv_to_json('data/lab05/samples/people.csv', 'data/lab05/out/people_from_csv.json')
"
```

Или:

```bash
python -m src.lab05.json_csv
```

### Пример входного `people.json`

```json
[
  {"name": "Alice", "age": 22, "city": "SPB"},
  {"name": "Bob", "age": 25, "city": "Moscow"},
  ...
]
```

### Результат `people_from_json.csv`

```csv
name,age,city
Alice,22,SPB
Bob,25,Moscow
...
```

---

## Задание B — CSV → XLSX
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab05/csv-%3Exlsx.png)
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab05/excel.png)
### `csv_to_xlsx(csv_path, xlsx_path)`

- Первая строка CSV — заголовок.
- Лист называется **Sheet1**.
- Автоширина колонок по длине текста (минимум 8 символов).
- Использует **openpyxl**.

### Запуск

```bash
python -c "
from src.lab05.csv_xlsx import csv_to_xlsx
csv_to_xlsx('data/lab05/samples/people.csv', 'data/lab05/out/people.xlsx')
"
```

Или:

```bash
python -m src.lab05.csv_xlsx
```

Откройте `data/lab05/out/people.xlsx` в Excel / LibreOffice и проверьте заголовки, данные и ширину столбцов.

---

## Политики ошибок

| Случай | Поведение |
|--------|-----------|
| Файл не найден | `FileNotFoundError` |
| Пустой JSON / не список словарей | `ValueError("Пустой JSON или неподдерживаемая структура")` |
| CSV без заголовка / пустой | `ValueError` |
| Неверное расширение файла | `ValueError` |
| Нет openpyxl | `RuntimeError` с подсказкой по установке |

Кодировка всегда **UTF-8**. Родительские директории создаются автоматически через `ensure_parent_dir` из ЛР4.

---

## Сценарии демонстрации

1. **JSON → CSV** — проверка заголовка и количества строк.
2. **CSV → JSON** — сравнение ключей и количества объектов.
3. **CSV → XLSX** — открытие файла в Excel/LibreOffice, проверка листа и ширины колонок.
