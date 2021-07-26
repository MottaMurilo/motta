# Primeiro e último nome de uma pessoa
import string

N =  str(input()).strip()
nome = N.split()
print(nome[0])
print(nome[(len(nome))-1])
