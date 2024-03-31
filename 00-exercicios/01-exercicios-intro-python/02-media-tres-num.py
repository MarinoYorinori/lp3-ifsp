#Ex02 - Escreva um programa em Python que solicita ao usuário três números e apresenta a média aritmética dos números informados.
n = (input("Insira numeros inteiros que deseja calcular a média (com espaço entre eles): ")).split()
n = [int(numero) for numero in n]
print(f"média: {sum(n)/len(n)}")