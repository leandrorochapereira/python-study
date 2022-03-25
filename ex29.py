'''num = int(input('Estou pensando em um número de 0 a 5, qual é? '))
if num == 2:
    print('Você acertou!')
else:
    print('Você errou! TENTE DE NOVO! ')
print('Outra vez?!')
'''
from random import randint
from time import sleep

pc = randint(0,5) #sorteio do numero
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Qual é ele? ')
print('-=-'*20)
jogador = int(input('Qual é o número? '))#inserção do número
print('PROCESSANDO...')
sleep(2)
if jogador == pc:
    print('Você acertou e ganhou :"""""( O número é {}'.format(pc))
else:
    print('Você é ruim! O número certo é {} e não {} HAHAHAHA!' .format(pc, jogador))