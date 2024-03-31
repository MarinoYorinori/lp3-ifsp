# Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo usuário.
def contador_palavras(frase):
    palavras = {}
    for palavra in frase:
        if palavra not in palavras:
            palavras[palavra] = 1
        else:
            palavras[palavra] += 1
    return palavras

print("------ Contador de palavras -------")
frase_usuario = input("Insira uma frase: ").lower()
frase_usuario = frase_usuario.split()
print(contador_palavras(frase_usuario))
