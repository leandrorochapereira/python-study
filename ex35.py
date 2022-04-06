#Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.

#podemos colocar cores no código da seguinte forma \033[      (finaliza com)m
#\033[(style);(texto);(background)m
#styles: 0 para none, 1 bold, 4 underline, 7 negative
#text 30 white, 31 red, 32 green, 33 yellow, 34 blue, 35 purple, 36 ciano, 37 gray
#background de 40 a 47 mesmas cores



r1 = float(input('\033[1;31;40mInsira a 1ª reta: '))
r2 = float(input('Insira a 2ª reta: '))
r3 = float(input('Insira a 3ª reta: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos acima PODEM formar um triângulo.')
else:
    print('\nOs segmentos acima NÃO PODEM formar um triângulo.')