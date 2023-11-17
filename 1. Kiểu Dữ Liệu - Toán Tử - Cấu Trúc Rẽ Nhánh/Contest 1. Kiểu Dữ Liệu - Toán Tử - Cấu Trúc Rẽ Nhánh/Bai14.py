a , b , c , d = map(float , input().split())
diemtb = (a + b + 2 * c + 3 * d) / 7
if diemtb >= 8:
    print('GIOI')
elif diemtb >= 6.5 and diemtb < 8:
    print('KHA')
elif diemtb >= 5 and diemtb < 6.5:
    print('TRUNG BINH')
else:
    print('YEU')