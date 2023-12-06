n = int(input())
for i in range(1 , n + 1):
    for j in range(1 , i + 1):
        print('*' , end = '')
    print()
print()
for i in range(1 , n + 1):
    for j in range(1 , n + 2 - i):
        print('*' , end = '')
    print()
print()
for i in range(1 , n + 1):
    for j in range(1 , n + 1):
        if j < n + 1 - i:
            print(' ' , end = '')
        else:
            print('*' , end = '')
    print()
print()
for i in range(1 , n + 1):
    for j in range(1 , n + 1):
        if i > j:
            print(' ' , end = '')
        else:
            print('*' , end = '')
    print()
print()
for i in range(1 , n + 1):
    for j in range(1 , i + 1):
        if i == 1 or i == n or j == 1 or j == i:
            print('*' , end = '')
        else:
            print(' ' , end = '')
    print()