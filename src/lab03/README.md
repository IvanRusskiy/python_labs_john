# ЛР3 тексты и частоты слов
## функция normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    делает всю строку по нижнему регистру, убирает лишние пробелы и невидимые символы
    '''
    if type(text) != str:
        raise TypeError('не тот тип данных')
    text_list = text.split()
    text = ''
    for txt in text_list:
        text += txt + ' '
    text = text[:-1]
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace('ё','е')
    if text == '':
        raise ValueError('пустая строка')
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
    '''
    возвращает список со всеми подстроками удовлетворяющими шаблону \w+(?:-\w+)*
    '''
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
    '''
    возвращает словарь с подсчитанными частотами слов
    '''
    if type(tokens) != list:
        raise TypeError('не правильный тип входных данных')
    if len(tokens) == 0:
        raise ValueError('пустой список')
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
    '''
    возвращает список со словами по убыванию их частоты, при равенстве частоты по алфавиту слова
    '''
    if type(freq) != list:
            raise TypeError('не правильный тип входных данных')
    if len(freq) == 0:
        raise ValueError('пустой список')
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
text_1 = input()

from src.lib.text import tokenize, top_n, count_freq, normalize

def text_stats(txt:str,flag:bool):
     '''
     функция выводит сводку по строке: сколько слов, сколько уникальных и тд
     при flag == 0 выводит по строчкам
     при flag == 1 выводит таблицей
     '''
     res = 'Всего слов:' + str(len(tokenize(txt))) + '\n'
     res = res + 'Уникальных слов:' + str(len(set(tokenize(txt)))) + '\n'
     res = res + 'Топ-5:' + '\n'
     if flag == 0:
          for word in top_n(tokenize(txt),n = 5)[::-1]:
               res = res + word[0] + ':' + str(word[1]) + '\n'
     else:
          mxlen = max([len(word[0]) for word in top_n(tokenize(txt),n = 5)[::-1]])
          a = 'слово'
          if mxlen < len(a):
               mxlen = len(a)
          res = res + a + ' '*(mxlen-len(a) + 1) + '|' + ' частота' + '\n'
          res = res + '-'*(mxlen + 1 + 8 + 1)+ '\n'
          for word in top_n(tokenize(txt),n = 5)[::-1]:
               res = res + word[0] + ' '*(mxlen-len(word[0]) + 1) + '|' + ' ' + str(word[1]) + '\n'
     return res

print(text_stats(text_1,1))
```
### запуск через терминал
```text
echo 'Привет, мир! Привет!!!' | python3 -m src.lab03.text_stats
```
### вывод
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/text_states.png)
### вывод(задание со звездочкой)
![](https://github.com/IvanRusskiy/python_labs_john/blob/main/images/lab03/text_states*.png)