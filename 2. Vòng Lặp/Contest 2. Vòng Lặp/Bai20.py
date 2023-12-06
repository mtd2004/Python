n = int(input())
if n == 1:
    print(-1)
else:
    print(n // 2)
    for i in range(1 , n // 2):
        print(2 , end = ' ')
    if n % 2 == 0:
        print(2)
    else:
        print(3)