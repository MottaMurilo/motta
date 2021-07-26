valor = int(input())
salario = int(input())
anos = int(input())

meses = anos*12  #Anos vezes meses, para pegar a mensalidade
casa = valor/meses  #Valor da prestação mensal
prestaçao = salario*0.30 #30% do salario dele que é o limite

if casa > prestaçao: #Caso prestação mensal for maior que 30% do salário será negado
    print('Negado')
else:
    print('Arpovado')