#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores


resp = 'S'
soma = quant = média = maior = menor = 0
#media dos valores eu tenho que somar os valores e a quantidade de valores, todas elas começam com 0
#logo podemos colocar desta forma = = =

while resp in 'Ss':
    num = int(input('Insira um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    resp = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]

média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print(f'O maior valor foi {maior} e o menor foi {menor}')