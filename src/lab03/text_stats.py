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

