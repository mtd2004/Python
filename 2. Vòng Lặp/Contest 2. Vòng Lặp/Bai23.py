n = int(input())
count = 1
for i in range(1 , n + 1):
    for j in range(1 , n + 1):
        print(count , end = ' ')
        count += 1
    print()
print()
for i in range(1 , n + 1):
    count = i
    for j in range(1 , n + 1):
        print(count , end = ' ')
        count += 1
    print()
print()
for i in range(1 , n + 1):
    for j in range(1 , n + 1):
        if j < n + 1 - i:
            print('~' , end = '')
        else:
            print(i , end = '')
    print()
print()
for i in range(1 , n + 1):
    count , res = i , n - 1
    for j in range(1 , i + 1):
        print(count , end = ' ')
        count += res
        res -= 1
    print()
