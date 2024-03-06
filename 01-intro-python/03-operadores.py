# Operadores 
# aritméticos = +, -, *, :, **, //

nota1 = 10
nota2 = 3
media = (nota1 + nota2) / 2

# Potencia
numero = 2 ** 3 # elevado ao cubo
numero = 10 ** 2 # elevado ao quadrado

# lógicos -------------------------------------------------------------------------------------------------------------
# and, or, not
# exp: acesso liberado = nao bloqueado, idade => 18, horario comercial (8 - 18)
bloqueado = False
idade = 21
hora_atual = 10

maior_idade = idade >= 18
horario_comercial = hora_atual >= 8 and hora_atual <= 18

if not bloqueado and maior_idade and horario_comercial:
    print('liberado')
else:
    print('nao liberado')

# operadores de comparação (funções que devolvem boolean) --------------------------------------------------------------
#   >, <, >=, <=, ==, =!, and 
numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) # True

#operador is
print(numero is numero) # False

numeros3 = [1, 2]
numeros4 = numeros3
print(numeros3 is numeros4) # True
print(numeros3 is not numeros4) # False

#operador in
print('a' in 'python') # False

prontuarios = ['SP001', 'SP002', 'SP003']
prontuario = 'SP002'
print(prontuario in prontuarios) # True

# sim, nao, talvez
opcao = ''
if opcao == 'sim' or opcao == 'nao' or opcao == 'talvez':
    print('opcao valida')
else:
    print('opcao invalida')

opcoes = ('sim', 'nao', 'talvez')
if opcao in opcoes:
    print('opcao valida')
else:
    print('opcao invalida')