# ЛР3 тексты и частоты слов
## функция normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text_list = text.split()
    text = ''
    for txt in text_list:
        text += txt + ' '
    text = text[:-1]
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace('ё','е')
    return text
```
### тест-кесы:
```python
print(normalize("ПрИвЕт\nМИр\t",casefold=True,yo2e=False))
print(normalize("ёжик, Ёлка",casefold=True,yo2e=True))
print(normalize("Hello\r\nWorld",casefold=True,yo2e=False))
print(normalize("  двойные   пробелы  ",casefold=False,yo2e=False))
```
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/normalize.png)
## функция tokenize
```python
import re
def tokenize(text: str) -> list[str]:
    text = normalize(text)
    return re.findall(r"\w+(?:-\w+)*", text)
```
### тест-кейсы:
```python
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/tokenize.png)
## функция count_freq
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    res = [[i,0] for i in set(tokens)]
    for x in res:
        for i in tokens:
            if i == x[0]:
                x[-1] += 1
    res.sort()
    result = {}
    for i in res:
        result.update({i[0]:i[1]})
    return result
```
### тест-кейсы:
```python
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
```
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/count_freq.png)
## функция top_n
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    res = [[i,0] for i in set(freq)]
    for x in res:
        for i in freq:
            if i == x[0]:
                x[-1] += 1
    res.sort()
    result = []
    for i in res:
            result.append((i[0],i[1]))
    return result[:n]
```
### тест-кейсы:
```python
print(top_n(["a","b","a","c","b","a"],n=2))
print(top_n(["bb","aa","bb","aa","cc"],n=2))
```
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/top_n.png)
## text_stats.py
```python
text_stats = input()

flag = 1

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

from lib import text

if text.top_n(text.tokenize(text_stats)) == []:
     raise ValueError("нет слов в строке") 

if flag == 0:
    print('Всего слов:' + str(len(text.tokenize(text_stats))))
    print('Уникальных слов:' + str(len(set(text.tokenize(text_stats)))))
    print('Топ-5:')
    for word in text.top_n(text.tokenize(text_stats),n = 5)[::-1]:
        print(word[0] + ':' + str(word[1]))
else:
    print('Всего слов:' + str(len(text.tokenize(text_stats))))
    print('Уникальных слов:' + str(len(set(text.tokenize(text_stats)))))
    print('Топ-5:')
    mxlen = max([len(word[0]) for word in text.top_n(text.tokenize(text_stats),n = 5)[::-1]])
    a = 'слово'
    if mxlen < len(a):
         mxlen = len(a)
    print(a + ' '*(mxlen-len(a) + 1) + '|' + ' частота')
    print('-'*(mxlen + 1 + 8 + 1))
    for word in text.top_n(text.tokenize(text_stats),n = 5)[::-1]:
            print(word[0] + ' '*(mxlen-len(word[0]) + 1) + '|' + ' ' + str(word[1]))
```
```text
current_dir — получает абсолютный путь к папке, где лежит сам скрипт.
parent_dir — поднимается на один уровень выше (в родительскую папку).
sys.path.insert(0, parent_dir) — ставит родительскую папку на первое место в списке поиска модулей.
```
### запуск через терминал
```text
echo 'Привет, мир! Привет!!!' | python3 src/lab03/text_stats.py
```
### вывод
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/text_states.png)
### вывод(задание со звездочкой)
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/text_states*.png)