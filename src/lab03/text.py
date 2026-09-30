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

# print(normalize("ПрИвЕт\nМИр\t",casefold=True,yo2e=False))
# print(normalize("ёжик, Ёлка",casefold=True,yo2e=True))
# print(normalize("Hello\r\nWorld",casefold=True,yo2e=False))
# print(normalize("  двойные   пробелы  ",casefold=False,yo2e=False))

def tokenize(text: str) -> list[str]:
    a = range(32,48) or range(58,65) or range(91,97) or range(123,126) and range(150)
    text = text + ' '
    str = ''
    res = []
    for i in text:
        if not(ord(i) in a) or i == '-':
            if ord(i) > 2000:
                continue
            else:
                str += i
        else:
            if str != '':
                res.append(str)
            str = ''
    return res

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    res = [[i,0] for i in set(tokens)]
    for x in res:
        for i in tokens:
            if i == x[0]:
                x[-1] += 1
    result = set()
    for i in res:
        result.add((i[0],i[1]))
    return result

print(count_freq(["a","b","a","c","b","a"]))

