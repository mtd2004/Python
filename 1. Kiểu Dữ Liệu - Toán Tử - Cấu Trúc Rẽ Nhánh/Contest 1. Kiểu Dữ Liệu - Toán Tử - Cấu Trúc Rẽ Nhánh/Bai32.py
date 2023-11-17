k2 , k3 , k5 , k6 = map(int , input().split())
count256 = min(k2 , k5 , k6)
count32 = min(abs(k2 - count256) , k3)
print(count256 * 256 + count32 * 32) 