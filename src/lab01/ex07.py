s = input("in:")
for i in range(0,len(s)):
    if 65 <= ord(s[i]) <= 90 or 1040 <= ord(s[i]) <= 1071:
        c = i
    if s[i] in '0123456789':
        e = i + 1 - c
        break
h = ''
while c + 1 <= len(s):
    h += s[c]
    c += e
print("out:" + h)