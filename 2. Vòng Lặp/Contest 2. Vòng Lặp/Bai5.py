n = int(input())
sum = 0
for i in range(1 , n + 1):
    sum += float(1) / i
sum /= 2
print('{:.5f}'.format(sum))