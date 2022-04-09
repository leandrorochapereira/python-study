# Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).



num = cont = soma = 0
num = int(input('Insira um número [digite 999 para parar]: '))

while num != 999:
    cont += 1 #quando um número for digitado, ele contará quantos números foram digitados
    #por isso ele começa com 0 fora do while
    soma += num
    #fazendo a soma de todos os números inseridos
    num = int(input('Insira um número [digite 999 para parar]: '))
    #deixando o num fora do lasso ele não soma o 999 do final e nem o adiciona a conta dos números
    
print('Foram digitados {} números e a soma entre eles é {}.'.format(cont,soma))