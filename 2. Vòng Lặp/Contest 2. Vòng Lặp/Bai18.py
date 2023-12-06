n = int(input())
count = 0
while n != 0:
    r = n % 10
    if r == 2 or r == 3 or r == 5 or r == 7:
        count += 1
    n //= 10
print(count)