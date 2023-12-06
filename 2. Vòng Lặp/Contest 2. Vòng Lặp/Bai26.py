a , b , n = map(int , input().split())
check = False
for i in range(0 , n // a + 1):
    if (n - a * i) % b == 0:
        print('YES')
        check = True
        break
if not check:
    print('NO')