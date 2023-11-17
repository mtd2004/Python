a , b , c , n = map(int , input().split())
ans = (a + b + c + n) // 3
if (a + b + c + n) % 3 == 0:
    if(ans >= a and ans >= b and ans >= c):
        print('YES')
    else:
        print('NO')
else:
    print('NO')