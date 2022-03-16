#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

med = float(input('Insira sua medida em metros: '))

print('Sua medida em cm é: {}cm \nSua medida em milímetros é: {}mm' .format(med * 100, med * 1000))