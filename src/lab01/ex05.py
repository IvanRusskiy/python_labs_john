fio = input('ФИО:')
ini = ''
c = 0
fio = fio.split()
for i in fio:
    ini += i[0].upper()
    c += len(i)
ini += '.'
print('Инициалы:',ini)
print('Длина:',c + 2)