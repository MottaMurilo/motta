from datetime import date
ano = date.today().year
nasc = int(input())
idade = ano - nasc
saldo = 18 - idade
saldo1 = idade - 18
anoalistar = ano - saldo1
plus = ano + saldo

if idade > 18:
    print('Você já deve ter se alistado em {}'.format(anoalistar))
elif idade < 18:
    print('Seu alistamento será em {}' .format(plus))
