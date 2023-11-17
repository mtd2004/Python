c = input()
if c >= 'A' and c <= 'Z':
    print('UPPER')
elif c >= 'a' and c <= 'z':
    print('LOWER')
elif c >= '0' and c <= '9':
    print('DIGIT')
else:
    print('SPECIAL')