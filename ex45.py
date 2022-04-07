#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randrange
from time import sleep

print('''SELECIONE SUA JOGADA
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA
''')
jogada = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

jogada2 = randrange(1, 4)
print('Eu escolhi: {}'.format(jogada2))

if jogada == 1 and jogada2 == 2:
    print('Eu ganhei! Papel ganha de Pedra! :)')
elif jogada == 1 and jogada2 == 3:
    print('Você ganhou! Pedra ganha de Tesoura! :)')
elif jogada == 2 and jogada2 == 1:
    print('Você ganhou! Papel ganha de Pedra! :(')
elif jogada == 2 and jogada2 == 3:
    print('Eu ganhei! Tesoura ganha de Papel! :)')
elif jogada == 3 and jogada2 == 2:
    print('Você ganhou! Tesoura ganha de Papel! :(')
elif jogada == 3 and jogada2 == 1:
    print('Eu ganhei! Pedra ganha de Tesoura! :)')
elif jogada == jogada2:
    print('Empatamos! Vamos de novo!')
else:
    print('Jogou errado! Jogue novamente! ')