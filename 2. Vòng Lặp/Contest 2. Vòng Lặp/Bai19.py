n = int(input())
chai = n // 28
vo = chai
while vo >= 3:
    chai += vo // 3
    vo = vo % 3 + vo // 3
print(chai)