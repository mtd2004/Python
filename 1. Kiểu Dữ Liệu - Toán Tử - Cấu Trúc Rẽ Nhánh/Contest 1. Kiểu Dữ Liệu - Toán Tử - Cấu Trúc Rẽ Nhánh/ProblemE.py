import math
a , b , c = map(int , input().split())
if a == 0:
    if b == 0:
        if c == 0:
            print('VO SO NGHIEM')
        else:
            print('VO NGHIEM')
    else:
        print('{:.2f}'.format(-c / b))
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print('VO NGHIEM')
    elif delta == 0:
        print('{:.2f}'.format(-b / (2 * a)))
    else:
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        print('{:.2f} {:.2f}'.format(x1 , x2))