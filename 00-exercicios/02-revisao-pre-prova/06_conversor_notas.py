print("------- Conversor de notas -------")
print("O programa converte notas em valor de 1 a 100 para o sistema em letras")
nota = float(input("\nInsira o valor da nota de 1 a 100: "))

notas = {
    1 : 'F - Péssimo, não aprovado',
    2 : 'D - Pode melhorar',
    3 : 'C - Bom',
    4 : 'B - Muito bom',
    5 : 'A - Perfeito!'
}

if nota >= 1 and nota <= 60:
    print(notas[1])
elif nota <= 70:
    print(notas[2])
elif nota <= 80:
    print(notas[3])
elif nota <= 90:
    print(notas[4])
elif nota <= 100:
    print(notas[5])
else:
    print('Insira um valor de 1 a 100')