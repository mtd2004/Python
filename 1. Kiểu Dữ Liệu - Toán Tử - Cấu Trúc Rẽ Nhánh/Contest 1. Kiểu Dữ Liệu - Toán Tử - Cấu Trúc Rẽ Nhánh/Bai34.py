c1 , c2 , c3 , c4 , c5 = map(int , input().split())
ans = (c1 + c2 + c3 + c4 + c5) // 5 
if (c1 + c2 + c3 + c4 + c5) % 5 == 0:
    if(ans != 0):
        print(ans)
    else:
        print(-1)
else:
    print(-1)