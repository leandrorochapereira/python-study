#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar 
# que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

r1 = float(input('Insira a \033[1;35m1ª\033[0m reta: '))
r2 = float(input('Insira a \033[1;31m2ª\033[0m reta: '))
r3 = float(input('Insira a \033[1;33m3ª\033[0m reta: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos acima \033[32mPODEM\033[0m formar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é \033[1;34mEQUILÁTERO\033[0m')
    elif r1 == r2 or r2 == r3 or r3 == r1: 
        print('O triângulo é \033[1;35mISÓSCELES\033[0m')
    else:
        print('O triângulo é \033[1;36mESCALENO\033[0m')
else:
    print('\nOs segmentos acima \033[1;31mNÃO PODEM\033[0m formar um triângulo.')