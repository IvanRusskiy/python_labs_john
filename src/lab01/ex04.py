m = int(input('Минуты:'))
a = m//60
print(str(a) + ':' + '0'*abs(len(str(m - 60*a)) - 2) + str(m - 60*a))