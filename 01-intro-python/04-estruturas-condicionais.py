#if, if/else, if/elif/else, ternario, match(switch mas mais poderoso)

'''
código do if:

if condição:
    codigo do if
    codigo do if

identação importante!!!!
'''

idade = 20
if idade >= 18:
    print ('Maior de idade')
    
# if/else/ elif ----------------------------------------------------------------------------------------------------
if idade >= 18:
    print('maior')
else:
    print('menor')

# elif (else if)
# crianca 0 - 12, adolescente 13 - 17, adulto 18 - 59, idoso 60+
idade = 30
if idade <= 12:
    print('crianca')
elif idade <= 17:
    print('adolescente')
elif idade <= 59:
    print('adulto')
else:
    print('idoso')

# Evitar alinhamento de if!!!
email = ''
senha = ''

if email == 'admin@email.com':
    if senha == '123admin':
        print('liberado')
    else: 
        print('email ou senha incorretos')
else:
    print('email ou senha incorretos')

# Ver melhorada
    if email == 'admin@email.com' and senha == '123admin':
        print('liberado')
    else:
        ('email ou senha incorretos')

# entrada numero 1, 2, 3 ...7
# saida dia segunda, terça, quarta ... sábado

dia = 4

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terca')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sábado')
#dicionario
dias = {
    1 : 'Domingo',
    2 : 'Segunda',
    3 : 'Terca',
    4 : 'Quarta',
    5 : 'Quinta',
    6 : 'Sexta',
    7 : 'Sábado',
}

if dia in dias:
    print(dias[dia])
else:
    print('dia inválido')

media = 8.0
if media >= 6.0:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

situacao = 'aprovado' if media >= 6.0 else 'reprovado'

# match ---------------------------------------------------------------------------------------------------------
match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terca')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Inválido')
# dia util 2, 3, 4, 5, 6
# fds 7, 1
match dia:
    case 1 | 7:
        print('fds')
    case 2 | 3 | 4 | 5:
        print('dia util')
    case _:
        print('bobo')
        
