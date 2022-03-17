#Escreva um programa que converta uma temperatura digitando em graus Celsius e 
# converta para graus Fahrenheit.

cels = float(input('Insira a temperatura em C°'))

fahr = ((cels * 9) / 5) + 32

print('A temperatura em Fahrenheit é: {}F°' .format(fahr))