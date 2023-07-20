import random
def cabecalho():
    print('-='*20)
    print(f'{"Bem vindo ao jogo de Forca":^40}')
    print('-='*20)


def imprime_perder(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}.")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def carrega_palavra():
    arquivo = open('palavras.txt', 'r')
    palavras = list()
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_ganha():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def jogar_forca():
    cabecalho()
    palavra_secreta = carrega_palavra()
    letras_acertadas = ['_' for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erro = 0
    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = str(input('Qual letra? ')).strip().upper()[0]
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra.upper():
                    letras_acertadas[index] = letra
                index += 1
        else:
            erro += 1
            desenha_forca(erro)
        enforcou = erro == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        imprime_ganha()
    else:
        imprime_perder(palavra_secreta)



if __name__ == '__main__':
    jogar_forca()
