#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.
#A hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
from math import hypot
catOpo = float(input('Insira o valor do cateto oposto: '))
catAdj = float(input('Insira o valor do cateto adjacente: '))

hip = hypot(catOpo, catAdj)
print('A hipotenusa vai medir {:.2f}.' .format(hip))