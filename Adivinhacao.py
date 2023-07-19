def jogar_advinhacao():
    from random import randint
    print('-='*20)
    print(f'{"Bem vindo ao jogo de Advinhação":^40}')
    print('-='*20)

    numero_secreto = randint(1,100)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nivel de dificuldade?')
    print('''    [1] Fácil
    [2] Médio
    [3] Difícil''')
    opc = int(input(('Selecione sua opção: ')))

    if opc == 1:
        total_de_tentativas = 20
    elif opc == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa: {rodada} de {total_de_tentativas}')
        chute = int(input('Digite o seu numero entre 1 e 100: '))
        if chute < 1 or chute > 100:
            print('Número inválido! Digite um número entre 1 e 100.')
            continue
        if numero_secreto == chute:
            print(f'Você acertou! Você fez {pontos} pontos!')
            break
        else:
            if chute > numero_secreto:
                print('Você errou! O seu chute foi maior que o numero sorteado')
            elif chute < numero_secreto:
                print('Você errou! O seu chute foi menor que o numero sorteado')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
    print('FIM DE JOGO!')


if __name__ == '__main__':
    jogar_advinhacao()
