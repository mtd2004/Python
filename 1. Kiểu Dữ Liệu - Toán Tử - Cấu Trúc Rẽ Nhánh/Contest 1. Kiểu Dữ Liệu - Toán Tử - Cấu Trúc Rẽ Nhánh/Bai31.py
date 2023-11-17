a1 , a2 , a3 , b1 , b2 , b3 = map(int , input().split())
n = int(input())
tongcup = a1 + a2 + a3 
tonghc = b1 + b2 + b3
ke1 = tongcup // 5
ke2 = tonghc // 10
if tongcup % 5 != 0:
    ke1 += 1
if tonghc % 10 != 0:
    ke2 += 1
if ke1 + ke2 <= n:
    print('YES')
else:
    print('NO')
    