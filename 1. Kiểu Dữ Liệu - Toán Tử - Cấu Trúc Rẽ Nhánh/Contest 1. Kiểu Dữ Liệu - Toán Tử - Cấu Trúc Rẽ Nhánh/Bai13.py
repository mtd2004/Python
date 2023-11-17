n = int(input())
nam = n // 365
tuan = (n % 365) // 7 
ngay = n - nam * 365 - tuan * 7
print(nam , tuan , ngay)