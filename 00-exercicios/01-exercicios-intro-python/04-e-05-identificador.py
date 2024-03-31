'''
Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.

Exemplos válidos:

    BR0001X
    BR1236X
    BR9999X

Exemplos inválidos:

    br0001X
    BR126X
    BR99999X
    BR9999Y
    
Crie uma função em Python que implementa essa verificação   
'''
def verifica_codigo(c):
    if len(c) != 7:
        return False
    elif c[0] != 'B' or c[1] != 'R' or c[len(c) - 1] != 'X':
        return False
    elif not int(c[2:6]):
        return False
    else:
        return True

# Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.
codigo = input("Insira o código identificador: ")
if verifica_codigo(codigo):
    print("Válido")
else:
    print("Inválido")
