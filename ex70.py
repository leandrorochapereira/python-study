#Crie um programa que leia o nome e o preço de vários produtos. 
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totCompra = 0

while True:
    nome = str(input('Insira o nome do produto: '))
    preço = float(input('Insira o valor do produto: '))

    cont = ' '
    while cont not in 'S':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print(f'{nome}')