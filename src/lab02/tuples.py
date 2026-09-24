def format_record(rec: tuple[str, str, float]) -> str:
    '''
    преобразует кортеж в строку
    выдает ошибку при пустой строке или неправильном типе GPA
    '''
    result = ''
    fio = rec[0].split()
    group = rec[1]
    gpa = rec[2]
    if fio == '' or group == '':
        raise ValueError("путая строка")
    if type(gpa) != float:
        raise TypeError("неверный тип GPA")
    result += fio[0][0].upper() + fio[0][1:] + ' '
    for i in range(0,len(fio)):
        if i != 0:
            result += fio[i][0].upper() + '.'
    result += ', гр. '
    result += group.strip()
    result += ', GPA '
    gpa = round(gpa,2)
    result += str(gpa)
    if len(str(gpa)[str(gpa).index('.') + 1:]) == 1:
        result += '0'
    return result

print(format_record(("Иванов Иван Иванович", "        BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "ABB-01", 3.999)))