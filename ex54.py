#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Insira o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas ainda não atingiram a maioridade.\n{} pessoas são maiores.'.format(menor, maior))