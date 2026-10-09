def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    делает всю строку по нижнему регистру, убирает лишние пробелы и невидимые символы
    '''
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

