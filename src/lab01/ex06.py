b = int(input('in_1:'))
h = []
s = 2
while True:
    a = input('in_' + str(s) + ':').split()
    s += 1
    if '-' in a:
        break
    h.append(a)
c = 0
k = 0
for i in h:
    if i[3] == 'True':
        c += 1
    else:
        k += 1
print(c,k)
