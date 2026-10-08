# ЛР3 тексты и частоты слов
# функция normalize
'''python
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
'''
