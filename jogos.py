import Forca
import Adivinhacao
from time import sleep

print('-='*10)
print(f'{"Escolha seu jogo":^20}')
print('-='*10)

print('''[1] - Forca
[2] - Advinhação ''')
opc = int(input('Qual jogo você deseja jogar? '))

if opc == 1:
    print('Abrindo Jogo da Forca...')
    sleep(1)
    print('Carregando...')
    sleep(1)
    Forca.jogar_forca()
elif opc == 2:
    print('Abrindo Jogo de Advinhação...')
    sleep(1)
    print('Carregando...')
    sleep(1)
    Adivinhacao.jogar_advinhacao()
