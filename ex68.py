#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de 
#vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

tipo = ' '
v = 0
while tipo not in 'PI':
    tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    if tipo == 'P':
        jogador = 'PAR'
        comp = 'IMPAR'
    elif tipo == 'I':
        jogador = 'IMPAR'
        comp = 'PAR'
    else:
        print('Escolha novamente')

    while True:
        valorjog = int(input('Insira um valor: '))
        valorcomp = randint(0,10)
        total = valorjog + valorcomp
        print('PAR OU ÍMPAR...')
        sleep(1.25)
        print(f'Você jogou {valorjog} e o computador jogou {valorcomp}. Total de {total}')

        if tipo == 'P' and total % 2 == 0:
            print('Você venceu! ')
            v += 1
        elif tipo == 'I' and total % 2 != 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu')
            break
        '''if tipo == 'I' and total % 2 != 0:
            print('Você ganhou!')
            v += 1'''
        '''else:
            print('Você perdeu!')
            break'''
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes! ')
