def format_record(fio: str, group: str, gpa: float):
    s = ''
    fio = fio.split()
    s += fio[0][0].upper() + fio[0][1:] + ' '
    for i in range(0,len(fio)):
        if i != 0:
            s += fio[i][0].upper() + '.'
    s += ', гр. '
    s += group
    s += ', GPA '
    gpa = round(gpa,2)
    s += str(gpa)
    if len(str(gpa)[str(gpa).index('.') + 1:]) == 1:
        s += '0'
    return s

print(format_record("  сидорова  анна   сергеевна ", "ABB-01", 3.999))