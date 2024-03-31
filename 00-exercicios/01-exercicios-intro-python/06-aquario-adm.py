'''
Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

    O volume do aquário em litros;
    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

Utilize funções.

'''
def calcular_volume(c, a, l):
    return (c * a * l)/1000

def calcular_potencia_termostato(vol, temp_des, temp_amb):
    return vol * 0.05 * (temp_des - temp_amb)

def calcular_filtragem(vol):
    min_max = [vol * 2 , vol * 3]
    return min_max

print("Administrador de aquário!")
c = float(input("Insira o comprimento (metros): "))
a = float(input("Insira a altura (metros): "))
l = float(input("Insira a largura (metros): "))
temp_des = float(input("Insira a temperatura desejada da água: "))
temp_amb = float(input("Insira a temperatura ambiente da água: "))
volume = calcular_volume(c,a,l)
print(f"O volume do seu aquário é de: {volume}")
print(f"A potência do termostato deve ser de: {calcular_potencia_termostato(volume, temp_des, temp_amb)}")
print(f"A quantidade de filtragem por hora deve ser de no mínimo {calcular_filtragem(volume)[0]} e no máximo {calcular_filtragem(volume)[1]}")