a , b , c = map(int , input().split())
if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print(1)
    elif a == b or a == c or b == c:
        print(2)
    elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print(3)
    else:
        print(4)
else:
    print('INVALID')