#Escreva um programa que leia dois números inteiros e compare-os. 
# mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Insira o \033[32m1º\033[0m número: '))
num2 = int(input('Insira o \033[31m2º\033[0m número: '))
if num1 > num2:
    print('O \033[32m1º\033[0m número é \033[32m{}\033[0m e é maior que o \033[31m2º: {}\033[0m.'.format(num1, num2))
elif num2 > num1:
    print('O \033[31m2º\033[0m número é \033[31m{}\033[0m e é maior que o \033[32m1º: {}\033[0m.'.format(num2, num1))
else:
    print('Os dois números são iguais. \033[32m{}\033[0m e \033[31m{}\033[0m.'.format(num1, num2))