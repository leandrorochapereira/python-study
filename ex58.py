#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, 
#mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('Estou pensando em um número entre 1 e 10.')
sleep(1)
print('Tente adivinhá-lo! ')
print('-' * 35)
pcnum = randint(0,10)
acertou = False
erro = 0
while not acertou:
    jognum = int(input('Qual é o número? '))
    erro += 1
    if jognum != pcnum:
        sleep(1)
        print('Você errou, tente novamente!')
        if pcnum > jognum:
            print('Mais...')
        else:
            print('Menos...')
    else:
        acertou = True
    
sleep(1)
print('Voce acertou! O número é {} com {} tentativas! '.format(pcnum, erro))