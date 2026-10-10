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