# Jogo da Adivinhação v.1.0

from random import choice

list = [0, 1, 2, 3, 4, 5]
list = random.choice(list)

x = int(input())

if x == list:
    print('Acertou')
else:
    print('Errou')



