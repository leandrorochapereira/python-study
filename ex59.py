'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
print('---- Insira 2 valores para realizar uma operação matemática ----\n')

num1 = int(input('Insira o 1º valor: '))
num2 = int(input('Insira o 2º valor: '))

prog = 0
result = 0

while prog != 5:
    print('''\nEscolha uma das operações matemáticas:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    prog = int(input('>>>>>>> Qual sua opção: '))
    if prog == 1:
        result = num1 + num2
        print('Você escolheu SOMAR.\n{} + {} = {}'.format(num1, num2, result))
    elif prog == 2:
        result = num1 * num2
        print('Você escolheu MULTIPLICAR.\n{} * {} = {}'.format(num1, num2, result))
    elif prog == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Você escolheu o MAIOR. Que é {}'.format(maior))
    elif prog == 4:
        print('---- Insira 2 valores para realizar uma operação matemática ----\n')
        num1 = int(input('Insira o 1º valor: '))
        num2 = int(input('Insira o 2º valor: '))
    elif prog == 5:
        print('-='*30)
        print('Você desejou fechar o programa. Obrigado.')
    else:
        print('-='*30)
        print('Comando inválido')
