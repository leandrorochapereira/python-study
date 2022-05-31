#Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

tot18 = totHm = totM20 = 0
while True:
#loop infinito
    idade = int(input('Idade: '))
    sexo = ' ' #inicia a variável sexo com vazio
    while sexo not in 'MF': #enquanto o sexo nao for M ou F ele vai continuar a ler
        sexo = str(input('Sexo: [M / F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totHm += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O total de pessoas maiores de 18 é: {tot18}')
print(f'O total de homens cadastrados é: {totHm}')
print(f'O total de mulheres menores de 20 é: {totM20}')