h = []
while True:
    a = input(), int(input()), input(bool)
    if a[0] == '' and a[1] == 0:
        break
    h.append(a)
c = 0
k = 0
for i in h:
    if i[2] == 'True':
        c += 1
    else:
        k += 1
print(c,k)
print(h)
