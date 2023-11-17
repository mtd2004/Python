n , m , a = map(int , input().split())
ans1 , ans2 = n // a , m // a
if n % a != 0:
    ans1 += 1
    
if m % a != 0:
    ans2 += 1
    
print(ans1 * ans2)