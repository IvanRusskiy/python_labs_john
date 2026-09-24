# ЛР2 коллекции и матрицы
## Задание A
### min_max(nums: list[float | int]) -> tuple[float | int, float | int]Вернуть кортеж (минимум, максимум). Если список пуст — ValueError. Использование встроенных функций min() и max() запрещено
![тест-кейсы:](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab02/exA-min_max.png)
### unique_sorted(nums: list[float | int]) -> list[float | int] Вернуть отсортированный список уникальных значений (по возрастанию). Использование встроенной функции sorted() / sort() запрещено
![тест-кейсы:](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab02/exA-unique_sorted.png)
### flatten(mat: list[list | tuple]) -> list «Расплющить» список списков/кортежей в один список по строкам (row-major). Если встретилась строка/элемент, который не является списком/кортежем — TypeError
![тест-кейсы:](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab02/exA-flatten.png)
## Задание B
### transpose(mat: list[list[float | int]]) -> list[list] Поменять строки и столбцы местами. Пустая матрица [] → []. Если матрица «рваная» (строки разной длины) — ValueError
![тест-кейсы:](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab02/exB-transpose.png)
### row_sums(mat: list[list[float | int]]) -> list[float] Сумма по каждой строке. Требуется прямоугольность (см. выше)
![тест-кейсы:](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab02/exB-row_sums.png)
### col_sums(mat: list[list[float | int]]) -> list[float] Сумма по каждому столбцу. Требуется прямоугольность.
![тест-кейсы:](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab02/exB-col_sums.png)
## Задание C
### Реализуйте format_record(rec: tuple[str, str, float]) -> str Вернуть строку вида: Иванов И.И., гр. BIVT-25, GPA 4.60
![тест-кейсы:](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab02/exC-format_record.png)