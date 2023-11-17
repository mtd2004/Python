a , b , c , d = map(int , input().split())
if b * b == a * c and c * c == b * d:
    print('YES')
else:
    print('NO')