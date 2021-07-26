nota = int(input())
nota1 = int(input())

media = (nota+nota1)/2

if media >= 7:
    print('Aprovado')
elif media >= 5 and media < 7:
    print('Recuperação')
else:
    print('Reprovado')