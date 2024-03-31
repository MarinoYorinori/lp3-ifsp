from random import randint
import sys

continuar = True
while continuar == True:
    print("\n\n------- Hangman! -------")
    print("Jogo da forca")

    forcas = {
        0: '',
        1: '\n\n/ \n',
        2: '\n\n/ \\\n',
        3: '\n | \n/ \\\n',
        4: '\n/| \n/ \\\n',
        5: '\n/|\\ \n/ \\\n',
        6: ' O\n/|\\ \n/ \\'
    }
    palavras = {
        0: ['latorre', 'professor de info'],
        1: ['quirino', 'professor de info'],
        2: ['god', 'referencia a funger (palavra em inglês)'],
        3: ['gato', 'animal'],
        4: ['jujuba', 'a gata mais foda q existe'],
        5: ['abacate', 'vegetal']
    }

    palavra = palavras[(randint(0, len(palavras)))]
    [print("_", end="") for letra in palavra[0]]
    print(f"\nDica: {palavra[1]}")

    erros = 0
    tentativa = ["_" for letra in palavra[0]]
    while erros <= len(forcas) - 1 and "".join(tentativa) != palavra[0]:
        letra = input("\nInsira uma letra: ").lower()
        if letra == "sair":
            sys.exit()
        elif letra not in palavra[0]:
            erros += 1
            print(forcas[erros])
        else:
            for i in range(len(palavra[0])):
                if palavra[0][i] == letra : tentativa[i] = letra
            print("".join(tentativa))

    if erros >= len(forcas) - 1:
        print("------ Perdeu bobão -------")
        print(f"A palavra era: {palavra[0]}")
    elif "".join(tentativa) == palavra[0]:
        print(f"------ Ganhou!! -------")
    else:
        print("Ocorreu algum erro...... tente novamente")
    
    if input("Deseja jogar novamente? (sim) (nao): ") == "sim":
        continuar = True
    else: 
        continuar = False