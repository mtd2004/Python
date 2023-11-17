c = input()
if c >= 'A' and c <= 'Z':
    print(chr(ord(c) + 32))
elif c >= 'a' and c <= 'z':
    print(chr(ord(c) - 32))
else:
    print(c)