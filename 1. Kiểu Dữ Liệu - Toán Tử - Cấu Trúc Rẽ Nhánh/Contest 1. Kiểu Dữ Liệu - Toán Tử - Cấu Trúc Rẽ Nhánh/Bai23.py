n , m = map(int , input().split())
maxn , minn = n , n // 2 
if n % 2 != 0:
    minn += 1
ans = (minn + m - 1) // m * m 
if ans <= maxn:
    print(ans)
else:
    print(-1)