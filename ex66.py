#Crie um programa que leia números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = cont = 0

while True:
    num = int(input('Insira um número [999 Para parar]: '))
    if num == 999:
        break
    #antes de somar verificamos se o num é 999 nossa flag
    #quando for, ele ignora o 999 e faz o cálculo
    cont += 1
    #contando quantos numeros, se for colocado antes da flag contará a flag
    soma += num
    #somando os números, se for colocado antes da flag, contará a flag
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
