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


import re
def tokenize(text: str) -> list[str]:
    '''
    возвращает список со всеми подстроками удовлетворяющими шаблону \w+(?:-\w+)*
    '''
    text = normalize(text)
    return re.findall(r"\w+(?:-\w+)*", text)

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


# print(normalize("ПрИвЕт\nМИр\t",casefold=True,yo2e=False))
# print(normalize("ёжик, Ёлка",casefold=True,yo2e=True))
# print(normalize("Hello\r\nWorld",casefold=True,yo2e=False))
# print(normalize("  двойные   пробелы  ",casefold=False,yo2e=False))

# def tokenize(text: str) -> list[str]:
#     a = range(32,48) or range(58,65) or range(91,97) or range(123,126) and range(150)
#     text = text + ' '
#     str = ''
#     res = []
#     for i in text:
#         if not(ord(i) in a) or i == '-':
#             if ord(i) > 2000:
#                 continue
#             else:
#                 str += i
#         else:
#             if str != '':
#                 res.append(str)
#             str = ''
#     return res


# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))


# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))


# print(top_n(["a","b","a","c","b","a"],n=2))
# print(top_n(["bb","aa","bb","aa","cc"],n=2))