#Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Insira a 1ª reta: '))
r2 = float(input('Insira a 2ª reta: '))
r3 = float(input('Insira a 3ª reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs segmentos acima PODEM formar um triângulo.')
else:
    print('\nOs segmentos acima NÃO PODEM formar um triângulo.')