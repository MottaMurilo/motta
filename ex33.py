
num, num2, num3 = input().split()

menor = num

if num < num2 and num < num3:
    menor = num
elif num2 < num and num2 < num3:
    menor = num2
else:
    menor = num3

maior = num
if num > num2 and num > num3:
    maior = num
elif num2 > num and num2 > num3:
    maior = num2
else:
    maior = num3

    print(menor)
    print(maior)