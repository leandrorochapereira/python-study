#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dol = float(input('Insira quanto está o dólar: $'))
din = float(input('Insira quanto dinheiro você tem na carteira: R$'))

print('Você possui ${:.2f} em dólares.' .format(din / dol))