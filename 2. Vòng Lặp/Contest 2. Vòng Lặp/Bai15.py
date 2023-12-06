from math import *
n = int(input())
res = 1
for i in range(1 , n + 1):
    res *= i
print(res)
# Ta có thể dùng print(factorial(n))