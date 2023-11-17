c = input()
if c >= 'A' and c <= 'Z':
    if(c == 'Z'):
        print('a')
    else:
        print(chr((ord(c) + 33)))
else:
    if(c == 'z'):
        print('a')
    else:
        print(chr((ord(c) + 1)))