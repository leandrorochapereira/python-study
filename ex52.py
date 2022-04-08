#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#(um número inteiro tem que dividir por 1 até ele e só 2x)
num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[0mO número {} foi divisível {}x'. format(num, tot))
if tot == 2:
    print('E por isso ele \033[1;34mÉ PRIMO.\033[0m')
else:
    print('E por isso ele \033[1;35mNÃO É PRIMO.\033[0m')