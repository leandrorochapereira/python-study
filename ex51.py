#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Insira o 1º termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro,décimo,razão):
    print('{} '.format(c), end='-> ')
print('End')
