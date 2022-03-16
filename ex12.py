#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
#com 5% de desconto.

pre = float(input('Insira o valor do produto em R$'))
desc = float(input('Insira a % de desconto: '))

print('Com {}% de desconto, você pagará: R${:.2f}' .format(desc, pre - (pre * desc / 100) ))