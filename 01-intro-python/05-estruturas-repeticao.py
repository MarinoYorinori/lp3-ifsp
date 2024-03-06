#for, while, (break/continue)

# for
for letra in 'Hello World':
    print(letra)

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# range (função)
# range(5) = 0, 1, 2, 3, 4
# range(start = 0, stop, step = 1)
# range(0, 12, 2) # 0, 2, 4, 6, 8, 10 - um for de 0 a 12, que vai de 2 em 2
for i in range(5):
    print(i)

# lista de 0 a 100
lista = list(range(101))
print(lista)

# while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break
comando = ''
while True:
    comando = input('Digite o comando')
    if comando == 'sair':
        break
    if comando == '1':
        print(1)

# continue
numeros = [-10, 3, 0, 5, -2]
for numero in numeros:
    if numero <= 0:
        continue 
    print(numero)

# compreensao de listas
numeros = [1, 2, 3, 4, 5]
quadrados = []

for numero in numeros:
    quadrados.append(numeros ** 2)

quadrados = [numero ** 2 for numero in numeros]

numeros = [-3, 0, 1, -5, 1, 2, 4]
positivos = [numero for numero in numeros if numero > 0] #um for normal no começo, com um filtro no final