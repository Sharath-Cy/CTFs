

given_String = "label"
flag = ''

for i in given_String:
    flag += chr(ord(i)^13)

print('crypto{{{}}}'.format(flag))