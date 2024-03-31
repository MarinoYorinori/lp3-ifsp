print("------- Verificador de palindromos! -------")
frase = input("Insira uma palavra ou frase: ")
frase = frase.lower()
LETRAS = "abcdefghijklmnopqrstuvwxyz"
for letra in frase:
    if letra not in LETRAS:
        frase = frase.replace(letra, "")

frase_contrario = [letra for letra in range(len(frase) -1, -1, -1)]
print(frase_contrario)

#"".join([frase[letra] for letra in range(len(frase) -1, -1,-1)])

if frase_contrario == frase:
    print("É palíndromo :3")
else:
    print(":3 ops (não é palíndromo)")