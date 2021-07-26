# Primeira e última ocorrência de uma string
import string
x = str(input()).upper().strip()


A1 = x.count('A')
A2 = x.find('A')+1
A3 = x.rfind('A')+1


print(A1, A2, A3)