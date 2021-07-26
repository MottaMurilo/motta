#BINARIO - OCTAL - HEXADECIMAL

num = int(input())
opcao = int(input())

if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])